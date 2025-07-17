from mcp.server.fastmcp import FastMCP
import tools

mcp = FastMCP("host info mcp")
mcp.add_tool(tools.get_host_info)

@mcp.tool()
def my_name():
    return "Zeyu Guan"

def main():
    mcp.run("stdio") # sse


if __name__ == "__main__":
    main()
