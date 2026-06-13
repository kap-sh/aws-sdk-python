"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerSigV4Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.mcp_tools_list


class MCPServerSigV4Configuration(TypedDict):
    tools: "aws_sdk_devops_agent.types.mcp_tools_list.MCPToolsList"
    """<p>List of MCP tools available for the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerSigV4Configuration) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.mcp_tools_list

    out["tools"] = aws_sdk_devops_agent.types.mcp_tools_list.serialize_json(
        value["tools"]
    )
    return out


def deserialize_json(data: dict) -> MCPServerSigV4Configuration:
    out: MCPServerSigV4Configuration = {}  # type: ignore[typeddict-item]
    if "tools" in data:
        import aws_sdk_devops_agent.types.mcp_tools_list

        out["tools"] = aws_sdk_devops_agent.types.mcp_tools_list.deserialize_json(
            data["tools"]
        )
    else:
        raise DeserializationError("MCPServerSigV4Configuration.tools required")
    return out
