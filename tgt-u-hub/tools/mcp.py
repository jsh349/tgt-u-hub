import numpy as np
import json
import time
import os

class MCP:
    def __init__(self, maxlen=100, results_path='results/results.jsonl'):
        self.history = []  # (step, data_type, content, notes, timestamp)
        self.cursor = 0
        self.maxlen = maxlen
        self.results_path = results_path
        os.makedirs(os.path.dirname(results_path), exist_ok=True)

    def update(self, step_number, data_type, content, notes=''):
        entry = (step_number, data_type, content, notes, time.time())
        self.history.append(entry)
        if len(self.history) > self.maxlen:
            self.history.pop(0)
        self.cursor = len(self.history) - 1
        if data_type in ['theory', 'code', 'feedback']:
            self._log_to_jsonl(step_number, data_type, content, notes)

    def get_current(self):
        return self.history[self.cursor] if self.history else None

    def move_cursor(self, delta):
        self.cursor = max(0, min(len(self.history) - 1, self.cursor + delta))

    def search(self, data_type):
        return [entry for entry in self.history if entry[1] == data_type]

    def _log_to_jsonl(self, step, data_type, content, notes):
        record = {
            "model": "grok4" if data_type in ['theory', 'review'] else "claude",
            "role": "theory" if data_type == 'theory' else "code" if data_type == 'code' else "feedback",
            "version": "TGT-U v1.1",
            "env": "tunneling_1d_double_well",
            "seed": 1337,
            "flags": {"tda": "on", "temp": "full", "renyi_alpha": 1.2},
            "kpi": {"message": notes},
            "invariance": {},
            "commit": "<git-sha>",
            "notes_url": "results/dashboards/latest.md",
            "timestamp": time.time()
        }
        with open(self.results_path, 'a') as f:
            if os.path.getsize(self.results_path) > 0:
                f.write('\n')
            json.dump(record, f)

# MCP 초기화
mcp = MCP(maxlen=100)
print("MCP 초기화 완료. 워크플로우 준비됨.")
