import pytest
from app import run_tool, run_workflow

def test_tool_allowlist():
    with pytest.raises(ValueError): run_tool('delete_files', 'hello')

def test_approval_gate():
    assert run_workflow('hello', ['count_words'], False)[0]['status'] == 'waiting_for_approval'
