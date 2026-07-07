"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilterValue``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)


class _FilterValue_stringValue(TypedDict, closed=True):
    stringValue: "str"


class _FilterValue_doubleValue(TypedDict, closed=True):
    doubleValue: "float"


class _FilterValue_booleanValue(TypedDict, closed=True):
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
