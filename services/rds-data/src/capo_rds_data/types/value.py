"""Generated from Smithy shape ``com.amazonaws.rdsdata#Value``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rds_data.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_rds_data.types.array_value_list
    import capo_rds_data.types.blob
    import capo_rds_data.types.boxed_boolean
    import capo_rds_data.types.boxed_double
    import capo_rds_data.types.boxed_float
    import capo_rds_data.types.boxed_integer
    import capo_rds_data.types.boxed_long
    import capo_rds_data.types.string
    import capo_rds_data.types.struct_value


class _Value_isNull(TypedDict, closed=True):
    isNull: "capo_rds_data.types.boxed_boolean.BoxedBoolean"


class _Value_bitValue(TypedDict, closed=True):
    bitValue: "capo_rds_data.types.boxed_boolean.BoxedBoolean"


class _Value_bigIntValue(TypedDict, closed=True):
    bigIntValue: "capo_rds_data.types.boxed_long.BoxedLong"


class _Value_intValue(TypedDict, closed=True):
    intValue: "capo_rds_data.types.boxed_integer.BoxedInteger"


class _Value_doubleValue(TypedDict, closed=True):
    doubleValue: "capo_rds_data.types.boxed_double.BoxedDouble"


class _Value_realValue(TypedDict, closed=True):
    realValue: "capo_rds_data.types.boxed_float.BoxedFloat"


class _Value_stringValue(TypedDict, closed=True):
    stringValue: "capo_rds_data.types.string.String"


class _Value_blobValue(TypedDict, closed=True):
    blobValue: "capo_rds_data.types.blob.Blob"


class _Value_arrayValues(TypedDict, closed=True):
    arrayValues: "capo_rds_data.types.array_value_list.ArrayValueList"


class _Value_structValue(TypedDict, closed=True):
    structValue: "capo_rds_data.types.struct_value.StructValue"


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
        import capo_rds_data.types.blob

        return {
            "blobValue": capo_rds_data.types.blob.serialize_json(value["blobValue"])
        }
    elif "arrayValues" in value:
        import capo_rds_data.types.array_value_list

        return {
            "arrayValues": capo_rds_data.types.array_value_list.serialize_json(
                value["arrayValues"]
            )
        }
    elif "structValue" in value:
        import capo_rds_data.types.struct_value

        return {
            "structValue": capo_rds_data.types.struct_value.serialize_json(
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
        import capo_rds_data.types.blob

        return {
            "blobValue": capo_rds_data.types.blob.deserialize_json(data["blobValue"])
        }
    elif "arrayValues" in data:
        import capo_rds_data.types.array_value_list

        return {
            "arrayValues": capo_rds_data.types.array_value_list.deserialize_json(
                data["arrayValues"]
            )
        }
    elif "structValue" in data:
        import capo_rds_data.types.struct_value

        return {
            "structValue": capo_rds_data.types.struct_value.deserialize_json(
                data["structValue"]
            )
        }
    else:
        raise DeserializationError("Value: no recognized variant key")
