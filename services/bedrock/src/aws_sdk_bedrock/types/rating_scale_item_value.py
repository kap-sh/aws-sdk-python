"""Generated from Smithy shape ``com.amazonaws.bedrock#RatingScaleItemValue``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError


class _RatingScaleItemValue_stringValue(TypedDict, closed=True):
    stringValue: "str"


class _RatingScaleItemValue_floatValue(TypedDict, closed=True):
    floatValue: "float"


RatingScaleItemValue: TypeAlias = (
    _RatingScaleItemValue_stringValue | _RatingScaleItemValue_floatValue
)


# --- restJson1 ser/de ---
def serialize_json(value: RatingScaleItemValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "floatValue" in value:
        return {"floatValue": value["floatValue"]}
    else:
        raise SerializationError("RatingScaleItemValue: no variant present")


def deserialize_json(data: dict) -> RatingScaleItemValue:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "floatValue" in data:
        return {"floatValue": data["floatValue"]}
    else:
        raise DeserializationError("RatingScaleItemValue: no recognized variant key")
