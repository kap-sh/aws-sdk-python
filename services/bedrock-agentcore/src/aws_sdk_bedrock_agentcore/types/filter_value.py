"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FilterValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.filter_string_value


class _FilterValue_stringValue(TypedDict):
    stringValue: "aws_sdk_bedrock_agentcore.types.filter_string_value.FilterStringValue"


class _FilterValue_doubleValue(TypedDict):
    doubleValue: "float"


class _FilterValue_booleanValue(TypedDict):
    booleanValue: "bool"


FilterValue: TypeAlias = (
    _FilterValue_stringValue | _FilterValue_doubleValue | _FilterValue_booleanValue
)


# --- restJson1 ser/de ---
def serialize_json(value: FilterValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    else:
        raise SerializationError("FilterValue: no variant present")


def deserialize_json(data: dict) -> FilterValue:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "doubleValue" in data:
        return {"doubleValue": data["doubleValue"]}
    elif "booleanValue" in data:
        return {"booleanValue": data["booleanValue"]}
    else:
        raise DeserializationError("FilterValue: no recognized variant key")
