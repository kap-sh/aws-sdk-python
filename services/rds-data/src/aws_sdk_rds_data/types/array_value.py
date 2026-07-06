"""Generated from Smithy shape ``com.amazonaws.rdsdata#ArrayValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_rds_data.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.array_of_array
    import aws_sdk_rds_data.types.boolean_array
    import aws_sdk_rds_data.types.double_array
    import aws_sdk_rds_data.types.long_array
    import aws_sdk_rds_data.types.string_array


class _ArrayValue_booleanValues(TypedDict, closed=True):
    booleanValues: "aws_sdk_rds_data.types.boolean_array.BooleanArray"


class _ArrayValue_longValues(TypedDict, closed=True):
    longValues: "aws_sdk_rds_data.types.long_array.LongArray"


class _ArrayValue_doubleValues(TypedDict, closed=True):
    doubleValues: "aws_sdk_rds_data.types.double_array.DoubleArray"


class _ArrayValue_stringValues(TypedDict, closed=True):
    stringValues: "aws_sdk_rds_data.types.string_array.StringArray"


class _ArrayValue_arrayValues(TypedDict, closed=True):
    arrayValues: "aws_sdk_rds_data.types.array_of_array.ArrayOfArray"


ArrayValue: TypeAlias = (
    _ArrayValue_booleanValues
    | _ArrayValue_longValues
    | _ArrayValue_doubleValues
    | _ArrayValue_stringValues
    | _ArrayValue_arrayValues
)


# --- restJson1 ser/de ---
def serialize_json(value: ArrayValue) -> dict:
    if "booleanValues" in value:
        import aws_sdk_rds_data.types.boolean_array

        return {
            "booleanValues": aws_sdk_rds_data.types.boolean_array.serialize_json(
                value["booleanValues"]
            )
        }
    elif "longValues" in value:
        import aws_sdk_rds_data.types.long_array

        return {
            "longValues": aws_sdk_rds_data.types.long_array.serialize_json(
                value["longValues"]
            )
        }
    elif "doubleValues" in value:
        import aws_sdk_rds_data.types.double_array

        return {
            "doubleValues": aws_sdk_rds_data.types.double_array.serialize_json(
                value["doubleValues"]
            )
        }
    elif "stringValues" in value:
        import aws_sdk_rds_data.types.string_array

        return {
            "stringValues": aws_sdk_rds_data.types.string_array.serialize_json(
                value["stringValues"]
            )
        }
    elif "arrayValues" in value:
        import aws_sdk_rds_data.types.array_of_array

        return {
            "arrayValues": aws_sdk_rds_data.types.array_of_array.serialize_json(
                value["arrayValues"]
            )
        }
    else:
        raise SerializationError("ArrayValue: no variant present")


def deserialize_json(data: dict) -> ArrayValue:
    if "booleanValues" in data:
        import aws_sdk_rds_data.types.boolean_array

        return {
            "booleanValues": aws_sdk_rds_data.types.boolean_array.deserialize_json(
                data["booleanValues"]
            )
        }
    elif "longValues" in data:
        import aws_sdk_rds_data.types.long_array

        return {
            "longValues": aws_sdk_rds_data.types.long_array.deserialize_json(
                data["longValues"]
            )
        }
    elif "doubleValues" in data:
        import aws_sdk_rds_data.types.double_array

        return {
            "doubleValues": aws_sdk_rds_data.types.double_array.deserialize_json(
                data["doubleValues"]
            )
        }
    elif "stringValues" in data:
        import aws_sdk_rds_data.types.string_array

        return {
            "stringValues": aws_sdk_rds_data.types.string_array.deserialize_json(
                data["stringValues"]
            )
        }
    elif "arrayValues" in data:
        import aws_sdk_rds_data.types.array_of_array

        return {
            "arrayValues": aws_sdk_rds_data.types.array_of_array.deserialize_json(
                data["arrayValues"]
            )
        }
    else:
        raise DeserializationError("ArrayValue: no recognized variant key")
