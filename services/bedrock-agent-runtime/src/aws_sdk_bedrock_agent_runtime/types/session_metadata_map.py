"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.session_metadata_key
    import aws_sdk_bedrock_agent_runtime.types.session_metadata_value

SessionMetadataMap: TypeAlias = dict[
    "aws_sdk_bedrock_agent_runtime.types.session_metadata_key.SessionMetadataKey",
    "aws_sdk_bedrock_agent_runtime.types.session_metadata_value.SessionMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SessionMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SessionMetadataMap:
    out: SessionMetadataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
