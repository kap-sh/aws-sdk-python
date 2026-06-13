"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventFieldValueUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.empty_field_value


class _AuditEventFieldValueUnion_stringValue(TypedDict):
    stringValue: "str"


class _AuditEventFieldValueUnion_doubleValue(TypedDict):
    doubleValue: "float"


class _AuditEventFieldValueUnion_booleanValue(TypedDict):
    booleanValue: "bool"


class _AuditEventFieldValueUnion_emptyValue(TypedDict):
    emptyValue: "aws_sdk_connectcases.types.empty_field_value.EmptyFieldValue"


class _AuditEventFieldValueUnion_userArnValue(TypedDict):
    userArnValue: "str"


AuditEventFieldValueUnion: TypeAlias = (
    _AuditEventFieldValueUnion_stringValue
    | _AuditEventFieldValueUnion_doubleValue
    | _AuditEventFieldValueUnion_booleanValue
    | _AuditEventFieldValueUnion_emptyValue
    | _AuditEventFieldValueUnion_userArnValue
)


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventFieldValueUnion) -> dict:
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
        raise SerializationError("AuditEventFieldValueUnion: no variant present")


def deserialize_json(data: dict) -> AuditEventFieldValueUnion:
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
        raise DeserializationError(
            "AuditEventFieldValueUnion: no recognized variant key"
        )
