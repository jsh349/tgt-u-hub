import os
from mcp import MCP  # tgt-u-hub/tools/mcp.py에서 가져옴

# MCP 초기화
results_path = 'results/results.jsonl'
os.makedirs(os.path.dirname(results_path), exist_ok=True)
mcp = MCP(maxlen=100, results_path=results_path)

# 초기 테스트
test_theory = "TGT-U v1.1 initial theory: PhaseNet with 5 Layers"
test_code = "def test_func(): pass"
test_feedback = "Initial setup looks good"

mcp.update(1, 'theory', test_theory, 'Test theory entry')
mcp.update(2, 'code', test_code, 'Test code entry')
mcp.update(3, 'feedback', test_feedback, 'Test feedback entry')

# 확인
print("Current MCP entry:", mcp.get_current())
print("Theory entries:", mcp.search('theory'))
print("Results JSONL exists:", os.path.exists(results_path))
