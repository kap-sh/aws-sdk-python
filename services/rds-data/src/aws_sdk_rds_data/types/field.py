"""Generated from Smithy shape ``com.amazonaws.rdsdata#Field``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_rds_data.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.array_value
    import aws_sdk_rds_data.types.blob
    import aws_sdk_rds_data.types.boxed_boolean
    import aws_sdk_rds_data.types.boxed_double
    import aws_sdk_rds_data.types.boxed_long
    import aws_sdk_rds_data.types.string


class _Field_isNull(TypedDict):
    isNull: "aws_sdk_rds_data.types.boxed_boolean.BoxedBoolean"


class _Field_booleanValue(TypedDict):
    booleanValue: "aws_sdk_rds_data.types.boxed_boolean.BoxedBoolean"


class _Field_longValue(TypedDict):
    longValue: "aws_sdk_rds_data.types.boxed_long.BoxedLong"


class _Field_doubleValue(TypedDict):
    doubleValue: "aws_sdk_rds_data.types.boxed_double.BoxedDouble"


class _Field_stringValue(TypedDict):
    stringValue: "aws_sdk_rds_data.types.string.String"


class _Field_blobValue(TypedDict):
    blobValue: "aws_sdk_rds_data.types.blob.Blob"


class _Field_arrayValue(TypedDict):
    arrayValue: "aws_sdk_rds_data.types.array_value.ArrayValue"


Field: TypeAlias = (
    _Field_isNull
    | _Field_booleanValue
    | _Field_longValue
    | _Field_doubleValue
    | _Field_stringValue
    | _Field_blobValue
    | _Field_arrayValue
)


# --- restJson1 ser/de ---
def serialize_json(value: Field) -> dict:
    if "isNull" in value:
        return {"isNull": value["isNull"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    elif "longValue" in value:
        return {"longValue": value["longValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "blobValue" in value:
        import aws_sdk_rds_data.types.blob

        return {
            "blobValue": aws_sdk_rds_data.types.blob.serialize_json(value["blobValue"])
        }
    elif "arrayValue" in value:
        import aws_sdk_rds_data.types.array_value

        return {
            "arrayValue": aws_sdk_rds_data.types.array_value.serialize_json(
                value["arrayValue"]
            )
        }
    else:
        raise SerializationError("Field: no variant present")


def deserialize_json(data: dict) -> Field:
    if "isNull" in data:
        return {"isNull": data["isNull"]}
    elif "booleanValue" in data:
        return {"booleanValue": data["booleanValue"]}
    elif "longValue" in data:
        return {"longValue": data["longValue"]}
    elif "doubleValue" in data:
        return {"doubleValue": data["doubleValue"]}
    elif "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "blobValue" in data:
        import aws_sdk_rds_data.types.blob

        return {
            "blobValue": aws_sdk_rds_data.types.blob.deserialize_json(data["blobValue"])
        }
    elif "arrayValue" in data:
        import aws_sdk_rds_data.types.array_value

        return {
            "arrayValue": aws_sdk_rds_data.types.array_value.deserialize_json(
                data["arrayValue"]
            )
        }
    else:
        raise DeserializationError("Field: no recognized variant key")
