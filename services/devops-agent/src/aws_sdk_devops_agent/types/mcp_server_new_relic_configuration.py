"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerNewRelicConfiguration``."""

from typing import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class MCPServerNewRelicConfiguration(TypedDict):
    account_id: "str"
    """<p>New Relic Account ID</p>"""
    endpoint: "str"
    """<p>MCP server endpoint URL (e.g., https://mcp.newrelic.com/mcp/)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerNewRelicConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> MCPServerNewRelicConfiguration:
    out: MCPServerNewRelicConfiguration = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("MCPServerNewRelicConfiguration.account_id required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("MCPServerNewRelicConfiguration.endpoint required")
    return out
