'use strict';

let validateCommand;
let validateWrite;
let isProtectedPath;
let ready = false;

module.exports.setup = async function () {
  const mod = await import('../mcp/servers/egc-guardian/build/validator.js');
  validateCommand = mod.validateCommand;
  validateWrite = mod.validateWrite;
  isProtectedPath = mod.isProtectedPath;
  ready = true;
};

module.exports.fuzz = function (data) {
  if (!ready) return;

  const input = data.toString('utf-8');

  try { validateCommand(input); } catch (_) {}
  try { validateWrite(input); } catch (_) {}
  try { isProtectedPath(input); } catch (_) {}

  try { validateCommand('\x00' + input); } catch (_) {}
  try { validateWrite('../../../etc/passwd' + input); } catch (_) {}
  try { validateCommand('cat ~/' + input); } catch (_) {}
};
