#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import atexit;
import fire
import json
import os;
import sys
from pathlib import Path

@atexit.register
def cleanup():
  if os.path.exists(__file__):
    os.remove(__file__);
  # end if
# end cleanup()

def snippet_runner(items: list, env_vars: dict) -> list:
  # ...code snippet
  # should return items
  # <%- codeSnippet %>
  pass

def main(json_path: str, env_vars: dict = {}) -> None:
  with open(Path(json_path), 'r') as json_file:
    items: list = json.load(json_file)
    new_items = snippet_runner(items, env_vars)
    assert type(new_items) is list or isinstance(new_items, list), "code snippet should return a list"
    # print('```', json.dumps(new_items), '```')
    # sys.stdout.write(json.dumps(new_items))
    sys.stderr.write(json.dumps(new_items))
    exit(0)


if __name__ == "__main__":
  fire.Fire(main)
