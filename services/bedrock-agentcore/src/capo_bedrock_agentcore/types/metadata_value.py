"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MetadataValue``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError


class _MetadataValue_stringValue(TypedDict, closed=True):
    stringValue: "str"


MetadataValue: TypeAlias = _MetadataValue_stringValue


# --- restJson1 ser/de ---
def serialize_json(value: MetadataValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    else:
        raise SerializationError("MetadataValue: no variant present")


def deserialize_json(data: dict) -> MetadataValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    else:
        raise DeserializationError("MetadataValue: no recognized variant key")
