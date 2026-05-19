'use strict';

const fs = require('fs');
const os = require('os');
const path = require('path');
const Database = require('better-sqlite3');

const { applyMigrations, getAppliedMigrations } = require('./migrations');
const { createQueryApi } = require('./queries');
const { assertValidEntity, validateEntity } = require('./schema');

const DEFAULT_STATE_STORE_RELATIVE_PATH = path.join('.gemini', 'egc', 'state.db');

function resolveStateStorePath(options = {}) {
  if (options.dbPath) {
    if (options.dbPath === ':memory:') {
      return options.dbPath;
    }
    return path.resolve(options.dbPath);
  }

  const homeDir = options.homeDir || process.env.HOME || os.homedir();
  return path.join(homeDir, DEFAULT_STATE_STORE_RELATIVE_PATH);
}

function sanitizeNamedParams(params) {
  if (params === null || params === undefined) {
    return params;
  }
  if (typeof params !== 'object' || Array.isArray(params)) {
    return params;
  }
  const sanitized = {};
  for (const [key, value] of Object.entries(params)) {
    sanitized[key] = value === undefined ? null : value;
  }
  return sanitized;
}

function wrapStatement(stmt) {
  return {
    all(...args) {
      return stmt.all(...args);
    },
    get(...args) {
      const row = stmt.get(...args);
      return row === undefined ? null : row;
    },
    run(params) {
      if (params && typeof params === 'object' && !Array.isArray(params)) {
        return stmt.run(sanitizeNamedParams(params));
      }
      if (params === undefined) {
        return stmt.run();
      }
      return stmt.run(params);
    },
  };
}

function wrapDatabase(rawDb) {
  return {
    exec(sql) {
      rawDb.exec(sql);
    },
    pragma(pragmaStr) {
      return rawDb.pragma(pragmaStr);
    },
    prepare(sql) {
      return wrapStatement(rawDb.prepare(sql));
    },
    transaction(fn) {
      return rawDb.transaction(fn);
    },
    close() {
      rawDb.close();
    },
  };
}

function openDatabase(dbPath) {
  if (dbPath !== ':memory:') {
    fs.mkdirSync(path.dirname(dbPath), { recursive: true });
  }

  const rawDb = new Database(dbPath);
  rawDb.pragma('foreign_keys = ON');
  if (dbPath !== ':memory:') {
    // WAL is not supported for in-memory databases.
    rawDb.pragma('journal_mode = WAL');
  }
  return wrapDatabase(rawDb);
}

async function createStateStore(options = {}) {
  const dbPath = resolveStateStorePath(options);
  const db = openDatabase(dbPath);
  const appliedMigrations = applyMigrations(db);
  const queryApi = createQueryApi(db);

  return {
    dbPath,
    close() {
      db.close();
    },
    getAppliedMigrations() {
      return getAppliedMigrations(db);
    },
    validateEntity,
    assertValidEntity,
    ...queryApi,
    _database: db,
    _migrations: appliedMigrations,
  };
}

module.exports = {
  DEFAULT_STATE_STORE_RELATIVE_PATH,
  createStateStore,
  resolveStateStorePath,
};
