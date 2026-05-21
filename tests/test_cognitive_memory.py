"""
Test suite for Cognitive Memory Infrastructure.
Verifies Local, Obsidian, and MCP providers, and the MemoryManager orchestration.
"""
import unittest
import os
import sys
import shutil
import tempfile
import json
from datetime import datetime
from pathlib import Path

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from llm.memory.base import MemoryEntry
from llm.memory.providers.local import LocalFileProvider
from llm.memory.providers.obsidian import ObsidianVaultProvider
from llm.memory.providers.mcp_obsidian import MCPObsidianProvider
from llm.memory.manager import MemoryManager

class TestCognitiveMemory(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.vault_dir = os.path.join(self.test_dir, "MyVault")
        os.makedirs(self.vault_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_local_provider(self):
        provider = LocalFileProvider(self.test_dir, namespace="TestEGC")
        self.assertTrue(provider.initialize())
        
        entry = MemoryEntry(
            title="Test Note",
            content="Hello World",
            category="Archaeology",
            tags=["test"],
            metadata={"source": "unittest"}
        )
        self.assertTrue(provider.write_note(entry))
        
        # Verify file existence
        note_path = Path(self.test_dir) / ".sessions" / "memory" / "TestEGC" / "Archaeology" / "Test_Note.md"
        self.assertTrue(note_path.exists())
        with open(note_path, "r") as f:
            content = f.read()
            self.assertIn("title: Test Note", content)
            self.assertIn("Hello World", content)

    def test_obsidian_provider(self):
        # Vault path must exist
        provider = ObsidianVaultProvider(self.vault_dir, namespace="EGC")
        self.assertTrue(provider.initialize())
        
        entry = MemoryEntry(
            title="Vault Entry",
            content="Vault Content",
            category="Sessions",
            tags=["vault"],
            metadata={}
        )
        self.assertTrue(provider.write_note(entry))
        
        # Verify
        note_path = Path(self.vault_dir) / "EGC" / "Sessions" / "Vault_Entry.md"
        self.assertTrue(note_path.exists())

    def test_mcp_provider_initialization(self):
        provider = MCPObsidianProvider(namespace="MCPTest", scope="full-vault")
        self.assertTrue(provider.initialize())
        self.assertEqual(provider.scope, "full-vault")
        self.assertEqual(provider.root_prefix, "")

    def test_mcp_provider_sandboxed(self):
        provider = MCPObsidianProvider(namespace="EGC", scope="sandboxed")
        self.assertEqual(provider.root_prefix, "EGC/")

    def test_manager_configuration(self):
        # Create a mock settings file
        settings = {
            "cognitiveMemory": {
                "enabled": True,
                "provider": "local",
                "namespace": "ManagerTest"
            }
        }
        settings_path = os.path.join(self.test_dir, "egc_settings.json")
        with open(settings_path, "w") as f:
            json.dump(settings, f)
            
        manager = MemoryManager(self.test_dir)
        self.assertIsNotNone(manager.provider)
        self.assertEqual(manager.provider.namespace, "ManagerTest")
        
        manager.record_session_start("test-123", {"user": "tester"})
        
        # Verify
        note_path = Path(self.test_dir) / ".sessions" / "memory" / "ManagerTest" / "Sessions" / "Session_test-123.md"
        self.assertTrue(note_path.exists())

    def test_manager_mcp_config(self):
        settings = {
            "cognitiveMemory": {
                "enabled": True,
                "provider": "obsidian-mcp",
                "scope": "full-vault"
            }
        }
        settings_path = os.path.join(self.test_dir, "egc_settings.json")
        with open(settings_path, "w") as f:
            json.dump(settings, f)
            
        manager = MemoryManager(self.test_dir)
        self.assertIsInstance(manager.provider, MCPObsidianProvider)
        self.assertEqual(manager.provider.scope, "full-vault")

if __name__ == "__main__":
    unittest.main()
