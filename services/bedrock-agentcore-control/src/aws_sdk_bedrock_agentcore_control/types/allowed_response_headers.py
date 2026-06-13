"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedResponseHeaders``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.http_header_name

AllowedResponseHeaders: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.http_header_name.HttpHeaderName"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedResponseHeaders) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedResponseHeaders:
    return list(data)