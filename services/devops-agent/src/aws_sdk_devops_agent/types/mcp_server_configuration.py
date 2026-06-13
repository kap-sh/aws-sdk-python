"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.mcp_tools_list


class MCPServerConfiguration(TypedDict):
    tools: "aws_sdk_devops_agent.types.mcp_tools_list.MCPToolsList"
    """<p>List of MCP tools can be used with the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.mcp_tools_list

    out["tools"] = aws_sdk_devops_agent.types.mcp_tools_list.serialize_json(
        value["tools"]
    )
    return out


def deserialize_json(data: dict) -> MCPServerConfiguration:
    out: MCPServerConfiguration = {}  # type: ignore[typeddict-item]
    if "tools" in data:
        import aws_sdk_devops_agent.types.mcp_tools_list

        out["tools"] = aws_sdk_devops_agent.types.mcp_tools_list.deserialize_json(
            data["tools"]
        )
    else:
        raise DeserializationError("MCPServerConfiguration.tools required")
    return out
