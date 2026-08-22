"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_metadata_shape

SessionMetadataList: TypeAlias = list[
    "capo_bedrock_agentcore.types.session_metadata_shape.SessionMetadataShape"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionMetadataList) -> list:
    import capo_bedrock_agentcore.types.session_metadata_shape

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.session_metadata_shape.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SessionMetadataList:
    import capo_bedrock_agentcore.types.session_metadata_shape

    out: SessionMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.session_metadata_shape.deserialize_json(item)
        )
    return out
