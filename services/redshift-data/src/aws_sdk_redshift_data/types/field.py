"""Generated from Smithy shape ``com.amazonaws.redshiftdata#Field``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_redshift_data.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.blob
    import aws_sdk_redshift_data.types.boxed_boolean
    import aws_sdk_redshift_data.types.boxed_double
    import aws_sdk_redshift_data.types.boxed_long
    import aws_sdk_redshift_data.types.string


class _Field_isNull(TypedDict, closed=True):
    isNull: "aws_sdk_redshift_data.types.boxed_boolean.BoxedBoolean"


class _Field_booleanValue(TypedDict, closed=True):
    booleanValue: "aws_sdk_redshift_data.types.boxed_boolean.BoxedBoolean"


class _Field_longValue(TypedDict, closed=True):
    longValue: "aws_sdk_redshift_data.types.boxed_long.BoxedLong"


class _Field_doubleValue(TypedDict, closed=True):
    doubleValue: "aws_sdk_redshift_data.types.boxed_double.BoxedDouble"


class _Field_stringValue(TypedDict, closed=True):
    stringValue: "aws_sdk_redshift_data.types.string.String"


class _Field_blobValue(TypedDict, closed=True):
    blobValue: "aws_sdk_redshift_data.types.blob.Blob"


Field: TypeAlias = (
    _Field_isNull
    | _Field_booleanValue
    | _Field_longValue
    | _Field_doubleValue
    | _Field_stringValue
    | _Field_blobValue
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Field) -> dict:
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
        import aws_sdk_redshift_data.types.blob

        return {
            "blobValue": aws_sdk_redshift_data.types.blob.serialize_aws_json_1_1(
                value["blobValue"]
            )
        }
    else:
        raise SerializationError("Field: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Field:
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
        import aws_sdk_redshift_data.types.blob

        return {
            "blobValue": aws_sdk_redshift_data.types.blob.deserialize_aws_json_1_1(
                data["blobValue"]
            )
        }
    else:
        raise DeserializationError("Field: no recognized variant key")
