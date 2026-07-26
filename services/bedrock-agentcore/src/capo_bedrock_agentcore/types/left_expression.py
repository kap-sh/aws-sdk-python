"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LeftExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.metadata_key


class _LeftExpression_metadataKey(TypedDict, closed=True):
    metadataKey: "capo_bedrock_agentcore.types.metadata_key.MetadataKey"


LeftExpression: TypeAlias = _LeftExpression_metadataKey


# --- restJson1 ser/de ---
def serialize_json(value: LeftExpression) -> dict:
    if "metadataKey" in value:
        return {"metadataKey": value["metadataKey"]}
    else:
        raise SerializationError("LeftExpression: no variant present")


def deserialize_json(data: dict) -> LeftExpression:
    if "metadataKey" in data:
        return {"metadataKey": data["metadataKey"]}
    else:
        raise DeserializationError("LeftExpression: no recognized variant key")
