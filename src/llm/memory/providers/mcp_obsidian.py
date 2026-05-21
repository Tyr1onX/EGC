"""
MCP-First implementation of the Cognitive Memory Provider for Obsidian.
Interacts with the user's full Obsidian vault via Model Context Protocol (MCP) tools.
"""
import os
import json
import logging
from typing import List, Optional, Any, Dict
from datetime import datetime

from llm.memory.base import CognitiveMemoryProvider, MemoryEntry

logger = logging.getLogger("EGC.Memory.MCP")

class MCPObsidianProvider(CognitiveMemoryProvider):
    """
    Cognitive Memory Provider using MCP to interact with Obsidian.
    Requires an active Obsidian MCP server (e.g., obsidian-mcp-server).
    """
    def __init__(self, namespace: str = "EGC", scope: str = "sandboxed"):
        self.namespace = namespace
        self.scope = scope  # 'sandboxed' or 'full-vault'
        self.root_prefix = f"{namespace}/" if scope == "sandboxed" else ""

    def initialize(self) -> bool:
        # Check if MCP tools are available in the runtime environment
        # This is a soft check, actual availability is confirmed on first call
        logger.info(f"Initializing MCP Obsidian Provider (Scope: {self.scope})")
        return True

    def _call_mcp_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Optional[Dict]:
        """
        Attempts to invoke an MCP tool.
        In the EGC runtime, this might be handled via a bridge or direct injection.
        """
        # Note: This is an architectural boundary. The real implementation would 
        # depend on how EGC exposes MCP tools to its Python runtime.
        # For now, we emit a structured log that an agent can pick up.
        logger.debug(f"MCP Call: {tool_name} with {json.dumps(arguments)}")
        
        # Implementation detail: If EGC has an MCP client, call it here.
        # Since we are in a transitional phase, we return None to signify 
        # that the automated bridge is not yet fully active.
        return None

    def write_note(self, entry: MemoryEntry) -> bool:
        target_path = f"{self.root_prefix}{entry.category}/{entry.title}.md"
        
        # Prepare content with Obsidian-friendly frontmatter
        content = f"---\ntitle: \"{entry.title}\"\ncategory: {entry.category}\ntags: [egc, {', '.join(entry.tags)}]\ntimestamp: {entry.timestamp.isoformat()}\n"
        for k, v in entry.metadata.items():
            content += f"{k}: \"{v}\"\n"
        content += f"---\n\n{entry.content}"

        logger.info(f"Writing note via MCP: {target_path}")
        
        # Try to use mcp__obsidian__create_note or similar
        res = self._call_mcp_tool("mcp__obsidian__create_note", {
            "path": target_path,
            "content": content
        })
        
        if res and res.get("success"):
            return True
            
        # Fallback: If MCP fails, we might want to log it or use another provider
        return False

    def append_journal(self, category: str, content: str) -> bool:
        target_path = f"{self.root_prefix}{category}/Journal.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_text = f"\n### {timestamp}\n\n{content}\n"

        logger.info(f"Appending to journal via MCP: {target_path}")
        
        res = self._call_mcp_tool("mcp__obsidian__append_content", {
            "path": target_path,
            "content": entry_text
        })
        
        if res and res.get("success"):
            return True
        return False

    def search_memory(self, query: str) -> List[MemoryEntry]:
        logger.info(f"Searching vault via MCP: {query}")
        
        res = self._call_mcp_tool("mcp__obsidian__search_notes", {
            "query": query
        })
        
        entries = []
        if res and isinstance(res.get("notes"), list):
            for note in res["notes"]:
                entries.append(MemoryEntry(
                    title=note.get("title", "Untitled"),
                    content=note.get("content", ""),
                    category="Search",
                    tags=[],
                    metadata={"path": note.get("path")}
                ))
        return entries

    def get_session_summary(self, session_id: str) -> Optional[str]:
        target_path = f"{self.root_prefix}Sessions/session_{session_id}.md"
        res = self._call_mcp_tool("mcp__obsidian__read_note", {
            "path": target_path
        })
        if res:
            return res.get("content")
        return None
