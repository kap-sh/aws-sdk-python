"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RequestHeaderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.request_header_allowlist


class _RequestHeaderConfiguration_requestHeaderAllowlist(TypedDict):
    requestHeaderAllowlist: "aws_sdk_bedrock_agentcore_control.types.request_header_allowlist.RequestHeaderAllowlist"


RequestHeaderConfiguration: TypeAlias = (
    _RequestHeaderConfiguration_requestHeaderAllowlist
)


# --- restJson1 ser/de ---
def serialize_json(value: RequestHeaderConfiguration) -> dict:
    if "requestHeaderAllowlist" in value:
        import aws_sdk_bedrock_agentcore_control.types.request_header_allowlist

        return {
            "requestHeaderAllowlist": aws_sdk_bedrock_agentcore_control.types.request_header_allowlist.serialize_json(
                value["requestHeaderAllowlist"]
            )
        }
    else:
        raise SerializationError("RequestHeaderConfiguration: no variant present")


def deserialize_json(data: dict) -> RequestHeaderConfiguration:
    if "requestHeaderAllowlist" in data:
        import aws_sdk_bedrock_agentcore_control.types.request_header_allowlist

        return {
            "requestHeaderAllowlist": aws_sdk_bedrock_agentcore_control.types.request_header_allowlist.deserialize_json(
                data["requestHeaderAllowlist"]
            )
        }
    else:
        raise DeserializationError(
            "RequestHeaderConfiguration: no recognized variant key"
        )
