"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordLeftExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.metadata_key


class _MemoryRecordLeftExpression_metadataKey(TypedDict, closed=True):
    metadataKey: "capo_bedrock_agentcore.types.metadata_key.MetadataKey"


MemoryRecordLeftExpression: TypeAlias = _MemoryRecordLeftExpression_metadataKey


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordLeftExpression) -> dict:
    if "metadataKey" in value:
        return {"metadataKey": value["metadataKey"]}
    else:
        raise SerializationError("MemoryRecordLeftExpression: no variant present")


def deserialize_json(data: dict) -> MemoryRecordLeftExpression:
    if data.get("metadataKey") is not None:
        return {"metadataKey": data["metadataKey"]}
    else:
        raise DeserializationError(
            "MemoryRecordLeftExpression: no recognized variant key"
        )
