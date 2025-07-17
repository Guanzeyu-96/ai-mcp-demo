# AI Agent Project

## Overview

MCP demo 项目，建议使用 claude desktop 作为 Agent。

## Installation

This Project is managed by uv, a Python package manager. To install the project dependencies, run:

```bash
uv install
```

Init project with:

```bash
uv init
```

Install the required packages:

```bash
uv sync
```

## Usage

Open settings and edit `claude_desktop_config.json` as:

```json
{
  "mcpServers": {
    "hostInfoMcp": {
      "command": "uv",
      "args": [
        "--directory",
        "${projectDir}",
        "run",
        "main.py"
      ]
    }
  }
}

## Extra tasking

我想在claude desktop中实现直接询问mock db中的内容。比如：
- 帮我查看Alice Zhang买了什么东西；
- 帮我查查所有买了USB-C Charger的用户的电话号码。
