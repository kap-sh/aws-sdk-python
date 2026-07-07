"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerAPIKeyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.api_key_value


class MCPServerAPIKeyConfig(TypedDict, closed=True):
    api_key_name: "str"
    """<p>User friendly API key name specified by end user.</p>"""
    api_key_value: "aws_sdk_devops_agent.types.api_key_value.ApiKeyValue"
    """<p>API key value for authenticating with the service.</p>"""
    api_key_header: "str"
    """<p>HTTP header name to send the API key in requests to the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerAPIKeyConfig) -> dict:
    out: dict = {}
    out["apiKeyName"] = value["api_key_name"]
    out["apiKeyValue"] = value["api_key_value"]
    out["apiKeyHeader"] = value["api_key_header"]
    return out


def deserialize_json(data: dict) -> MCPServerAPIKeyConfig:
    out: MCPServerAPIKeyConfig = {}  # type: ignore[typeddict-item]
    if "apiKeyName" in data:
        out["api_key_name"] = data["apiKeyName"]
    else:
        raise DeserializationError("MCPServerAPIKeyConfig.api_key_name required")
    if "apiKeyValue" in data:
        out["api_key_value"] = data["apiKeyValue"]
    else:
        raise DeserializationError("MCPServerAPIKeyConfig.api_key_value required")
    if "apiKeyHeader" in data:
        out["api_key_header"] = data["apiKeyHeader"]
    else:
        raise DeserializationError("MCPServerAPIKeyConfig.api_key_header required")
    return out
