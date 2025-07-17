# AI MCP Demo

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

Take Claude Desktop as an example, you can start the MCP server by open settings and edit `claude_desktop_config.json` as:

```json
{
  "mcpServers": {
    "hostInfoMcp": {
      "command": "uv",
      "args": ["--directory", "${projectDir}", "run", "main.py"]
    }
  }
}
```

## Extra tasking

我想在 claude desktop 中实现直接询问 mock db 中的内容。比如：

- 帮我查看 Yaxin 买了什么东西；
- 帮我查查所有买了 USB-C Charger 的用户。
- PS5 出问题了，给所有买了 PS5 的用户打电话。
