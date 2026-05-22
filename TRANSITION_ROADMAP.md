# EGC Transition Roadmap

## Overview
This roadmap outlines the structured path from the Gemini CLI era to the Antigravity future. Technical migration work has NOT started yet and depends on ongoing compatibility research and runtime auditing.

### Phase 0: Legacy Stabilization (CURRENT)
- Freeze current Gemini-compatible generation.
- Create preservation Git tags.
- Document legacy support policy.
- Establish archival artifacts.

### Phase 1: Discovery & Compatibility Audit
- Comprehensive analysis of Antigravity runtime capabilities.
- Mapping Gemini CLI command structures to MCP-native primitives.
- Identifying breaking changes in tool execution and observation loops.

### Phase 2: Adapter Layer Design
- Design of a backward-compatibility layer.
- Prototyping "Gemini-to-Antigravity" shim for legacy skills.
- Definition of the EGC-MCP Bridge specification.

### Phase 3: MCP Normalization
- Refactoring internal registries to follow standard MCP resource and tool patterns.
- Decoupling execution logic from specific CLI runtimes.
- Enhancing behavioral manifests for multi-host compatibility.

### Phase 4: Antigravity Runtime Support
- Official support for Antigravity as a primary runtime.
- Validation of all legacy skills and hooks in the new environment.
- Final transition release.

---
*Note: Each phase will be preceded by a formal technical review and documentation update.*
