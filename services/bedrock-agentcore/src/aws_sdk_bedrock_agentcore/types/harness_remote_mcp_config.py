"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessRemoteMcpConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_remote_mcp_url
    import aws_sdk_bedrock_agentcore.types.http_headers_map


class HarnessRemoteMcpConfig(TypedDict, closed=True):
    url: "aws_sdk_bedrock_agentcore.types.harness_remote_mcp_url.HarnessRemoteMcpUrl"
    """<p>URL of the MCP endpoint.</p>"""
    headers: NotRequired[
        "aws_sdk_bedrock_agentcore.types.http_headers_map.HttpHeadersMap"
    ]
    """<p>Custom headers to include when connecting to the remote MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessRemoteMcpConfig) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "headers" in value:
        import aws_sdk_bedrock_agentcore.types.http_headers_map

        out["headers"] = (
            aws_sdk_bedrock_agentcore.types.http_headers_map.serialize_json(
                value["headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessRemoteMcpConfig:
    out: HarnessRemoteMcpConfig = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("HarnessRemoteMcpConfig.url required")
    if "headers" in data:
        import aws_sdk_bedrock_agentcore.types.http_headers_map

        out["headers"] = (
            aws_sdk_bedrock_agentcore.types.http_headers_map.deserialize_json(
                data["headers"]
            )
        )
    return out
