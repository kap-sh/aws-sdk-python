"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RequestHeaderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.request_header_allowlist


class _RequestHeaderConfiguration_requestHeaderAllowlist(TypedDict, closed=True):
    requestHeaderAllowlist: "capo_bedrock_agentcore_control.types.request_header_allowlist.RequestHeaderAllowlist"


RequestHeaderConfiguration: TypeAlias = (
    _RequestHeaderConfiguration_requestHeaderAllowlist
)


# --- restJson1 ser/de ---
def serialize_json(value: RequestHeaderConfiguration) -> dict:
    if "requestHeaderAllowlist" in value:
        import capo_bedrock_agentcore_control.types.request_header_allowlist

        return {
            "requestHeaderAllowlist": capo_bedrock_agentcore_control.types.request_header_allowlist.serialize_json(
                value["requestHeaderAllowlist"]
            )
        }
    else:
        raise SerializationError("RequestHeaderConfiguration: no variant present")


def deserialize_json(data: dict) -> RequestHeaderConfiguration:
    if data.get("requestHeaderAllowlist") is not None:
        import capo_bedrock_agentcore_control.types.request_header_allowlist

        return {
            "requestHeaderAllowlist": capo_bedrock_agentcore_control.types.request_header_allowlist.deserialize_json(
                data["requestHeaderAllowlist"]
            )
        }
    else:
        raise DeserializationError(
            "RequestHeaderConfiguration: no recognized variant key"
        )
