"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValueUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.empty_field_value


class _FieldValueUnion_stringValue(TypedDict):
    stringValue: "str"


class _FieldValueUnion_doubleValue(TypedDict):
    doubleValue: "float"


class _FieldValueUnion_booleanValue(TypedDict):
    booleanValue: "bool"


class _FieldValueUnion_emptyValue(TypedDict):
    emptyValue: "aws_sdk_connectcases.types.empty_field_value.EmptyFieldValue"


class _FieldValueUnion_userArnValue(TypedDict):
    userArnValue: "str"


FieldValueUnion: TypeAlias = (
    _FieldValueUnion_stringValue
    | _FieldValueUnion_doubleValue
    | _FieldValueUnion_booleanValue
    | _FieldValueUnion_emptyValue
    | _FieldValueUnion_userArnValue
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueUnion) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    elif "emptyValue" in value:
        import aws_sdk_connectcases.types.empty_field_value

        return {
            "emptyValue": aws_sdk_connectcases.types.empty_field_value.serialize_json(
                value["emptyValue"]
            )
        }
    elif "userArnValue" in value:
        return {"userArnValue": value["userArnValue"]}
    else:
        raise SerializationError("FieldValueUnion: no variant present")


def deserialize_json(data: dict) -> FieldValueUnion:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "doubleValue" in data:
        return {"doubleValue": data["doubleValue"]}
    elif "booleanValue" in data:
        return {"booleanValue": data["booleanValue"]}
    elif "emptyValue" in data:
        import aws_sdk_connectcases.types.empty_field_value

        return {
            "emptyValue": aws_sdk_connectcases.types.empty_field_value.deserialize_json(
                data["emptyValue"]
            )
        }
    elif "userArnValue" in data:
        return {"userArnValue": data["userArnValue"]}
    else:
        raise DeserializationError("FieldValueUnion: no recognized variant key")
