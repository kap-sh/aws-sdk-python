"""Generated from Smithy shape ``com.amazonaws.xray#AnnotationValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_xray.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_boolean
    import aws_sdk_xray.types.nullable_double
    import aws_sdk_xray.types.string


class _AnnotationValue_NumberValue(TypedDict):
    NumberValue: "aws_sdk_xray.types.nullable_double.NullableDouble"


class _AnnotationValue_BooleanValue(TypedDict):
    BooleanValue: "aws_sdk_xray.types.nullable_boolean.NullableBoolean"


class _AnnotationValue_StringValue(TypedDict):
    StringValue: "aws_sdk_xray.types.string.String"


AnnotationValue: TypeAlias = (
    _AnnotationValue_NumberValue
    | _AnnotationValue_BooleanValue
    | _AnnotationValue_StringValue
)


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationValue) -> dict:
    if "NumberValue" in value:
        return {"NumberValue": value["NumberValue"]}
    elif "BooleanValue" in value:
        return {"BooleanValue": value["BooleanValue"]}
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    else:
        raise SerializationError("AnnotationValue: no variant present")


def deserialize_json(data: dict) -> AnnotationValue:
    if "NumberValue" in data:
        return {"NumberValue": data["NumberValue"]}
    elif "BooleanValue" in data:
        return {"BooleanValue": data["BooleanValue"]}
    elif "StringValue" in data:
        return {"StringValue": data["StringValue"]}
    else:
        raise DeserializationError("AnnotationValue: no recognized variant key")
