import os
import re
import unittest

class TestGitHubProfile(unittest.TestCase):
    def setUp(self):
        self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.readme_path = os.path.join(self.workspace_root, "README.md")
        self.workflow_path = os.path.join(self.workspace_root, ".github", "workflows", "metrics.yml")

    def test_readme_exists(self):
        self.assertTrue(os.path.exists(self.readme_path), "README.md does not exist")

    def test_workflow_exists_and_looks_valid(self):
        self.assertTrue(os.path.exists(self.workflow_path), "metrics.yml workflow does not exist")
        with open(self.workflow_path, 'r') as f:
            content = f.read()
        self.assertTrue(content.strip().startswith("---") or "name:" in content, "metrics.yml is not a valid YAML/workflow file structure")

    def test_referenced_local_images_exist(self):
        with open(self.readme_path, 'r') as f:
            content = f.read()
        
        # Match src="./images/..." or src="images/..."
        matches = re.findall(r'src=["\']\s*(\./images/[a-zA-Z0-9_\-\.]+)\s*["\']', content)
        matches.extend(re.findall(r'src=["\']\s*(images/[a-zA-Z0-9_\-\.]+)\s*["\']', content))
        
        for match in matches:
            # Clean up match
            clean_path = match.lstrip("./")
            abs_img_path = os.path.join(self.workspace_root, clean_path)
            self.assertTrue(os.path.exists(abs_img_path), f"Referenced image {clean_path} does not exist in filesystem")

    def test_readme_structure_headers(self):
        with open(self.readme_path, 'r') as f:
            content = f.read()
        
        # We expect specific headers to structure the profile README
        self.assertIn("## :wave: About Me", content, "Missing '## :wave: About Me' section")
        self.assertIn("## :rocket: Skills Overview", content, "Missing '## :rocket: Skills Overview' section")
        self.assertIn("## :bar_chart: Coding Activity & Metrics", content, "Missing '## :bar_chart: Coding Activity & Metrics' section")

    def test_taskfile_exists_and_has_required_tasks(self):
        taskfile_path = os.path.join(self.workspace_root, "Taskfile.yaml")
        self.assertTrue(os.path.exists(taskfile_path), "Taskfile.yaml does not exist")
        with open(taskfile_path, 'r') as f:
            content = f.read()
        self.assertIn("default:", content, "Taskfile missing 'default' task")
        self.assertIn("test:", content, "Taskfile missing 'test' task")
        self.assertIn("check:", content, "Taskfile missing 'check' task")

    def test_ci_test_workflow_exists_and_looks_valid(self):
        workflow_path = os.path.join(self.workspace_root, ".github", "workflows", "test.yml")
        self.assertTrue(os.path.exists(workflow_path), "test.yml CI workflow does not exist")
        with open(workflow_path, 'r') as f:
            content = f.read()
        self.assertIn("task check", content, "test.yml is missing 'task check' execution step")

    def test_linter_configs_exist(self):
        yamllint_path = os.path.join(self.workspace_root, ".yamllint")
        markdownlint_path = os.path.join(self.workspace_root, ".markdownlint.yaml")
        self.assertTrue(os.path.exists(yamllint_path), ".yamllint does not exist")
        self.assertTrue(os.path.exists(markdownlint_path), ".markdownlint.yaml does not exist")

    def test_spellcheck_configs_exist(self):
        typos_path = os.path.join(self.workspace_root, "_typos.toml")
        self.assertTrue(os.path.exists(typos_path), "_typos.toml does not exist")

if __name__ == "__main__":
    unittest.main()
