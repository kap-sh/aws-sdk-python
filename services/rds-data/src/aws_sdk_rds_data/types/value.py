"""Generated from Smithy shape ``com.amazonaws.rdsdata#Value``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_rds_data.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.array_value_list
    import aws_sdk_rds_data.types.blob
    import aws_sdk_rds_data.types.boxed_boolean
    import aws_sdk_rds_data.types.boxed_double
    import aws_sdk_rds_data.types.boxed_float
    import aws_sdk_rds_data.types.boxed_integer
    import aws_sdk_rds_data.types.boxed_long
    import aws_sdk_rds_data.types.string
    import aws_sdk_rds_data.types.struct_value


class _Value_isNull(TypedDict):
    isNull: "aws_sdk_rds_data.types.boxed_boolean.BoxedBoolean"


class _Value_bitValue(TypedDict):
    bitValue: "aws_sdk_rds_data.types.boxed_boolean.BoxedBoolean"


class _Value_bigIntValue(TypedDict):
    bigIntValue: "aws_sdk_rds_data.types.boxed_long.BoxedLong"


class _Value_intValue(TypedDict):
    intValue: "aws_sdk_rds_data.types.boxed_integer.BoxedInteger"


class _Value_doubleValue(TypedDict):
    doubleValue: "aws_sdk_rds_data.types.boxed_double.BoxedDouble"


class _Value_realValue(TypedDict):
    realValue: "aws_sdk_rds_data.types.boxed_float.BoxedFloat"


class _Value_stringValue(TypedDict):
    stringValue: "aws_sdk_rds_data.types.string.String"


class _Value_blobValue(TypedDict):
    blobValue: "aws_sdk_rds_data.types.blob.Blob"


class _Value_arrayValues(TypedDict):
    arrayValues: "aws_sdk_rds_data.types.array_value_list.ArrayValueList"


class _Value_structValue(TypedDict):
    structValue: "aws_sdk_rds_data.types.struct_value.StructValue"


Value: TypeAlias = (
    _Value_isNull
    | _Value_bitValue
    | _Value_bigIntValue
    | _Value_intValue
    | _Value_doubleValue
    | _Value_realValue
    | _Value_stringValue
    | _Value_blobValue
    | _Value_arrayValues
    | _Value_structValue
)


# --- restJson1 ser/de ---
def serialize_json(value: Value) -> dict:
    if "isNull" in value:
        return {"isNull": value["isNull"]}
    elif "bitValue" in value:
        return {"bitValue": value["bitValue"]}
    elif "bigIntValue" in value:
        return {"bigIntValue": value["bigIntValue"]}
    elif "intValue" in value:
        return {"intValue": value["intValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "realValue" in value:
        return {"realValue": value["realValue"]}
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "blobValue" in value:
        import aws_sdk_rds_data.types.blob

        return {
            "blobValue": aws_sdk_rds_data.types.blob.serialize_json(value["blobValue"])
        }
    elif "arrayValues" in value:
        import aws_sdk_rds_data.types.array_value_list

        return {
            "arrayValues": aws_sdk_rds_data.types.array_value_list.serialize_json(
                value["arrayValues"]
            )
        }
    elif "structValue" in value:
        import aws_sdk_rds_data.types.struct_value

        return {
            "structValue": aws_sdk_rds_data.types.struct_value.serialize_json(
                value["structValue"]
            )
        }
    else:
        raise SerializationError("Value: no variant present")


def deserialize_json(data: dict) -> Value:
    if "isNull" in data:
        return {"isNull": data["isNull"]}
    elif "bitValue" in data:
        return {"bitValue": data["bitValue"]}
    elif "bigIntValue" in data:
        return {"bigIntValue": data["bigIntValue"]}
    elif "intValue" in data:
        return {"intValue": data["intValue"]}
    elif "doubleValue" in data:
        return {"doubleValue": data["doubleValue"]}
    elif "realValue" in data:
        return {"realValue": data["realValue"]}
    elif "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "blobValue" in data:
        import aws_sdk_rds_data.types.blob

        return {
            "blobValue": aws_sdk_rds_data.types.blob.deserialize_json(data["blobValue"])
        }
    elif "arrayValues" in data:
        import aws_sdk_rds_data.types.array_value_list

        return {
            "arrayValues": aws_sdk_rds_data.types.array_value_list.deserialize_json(
                data["arrayValues"]
            )
        }
    elif "structValue" in data:
        import aws_sdk_rds_data.types.struct_value

        return {
            "structValue": aws_sdk_rds_data.types.struct_value.deserialize_json(
                data["structValue"]
            )
        }
    else:
        raise DeserializationError("Value: no recognized variant key")
