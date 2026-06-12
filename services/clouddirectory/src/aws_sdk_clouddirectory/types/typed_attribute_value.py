"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.binary_attribute_value
    import aws_sdk_clouddirectory.types.boolean_attribute_value
    import aws_sdk_clouddirectory.types.datetime_attribute_value
    import aws_sdk_clouddirectory.types.number_attribute_value
    import aws_sdk_clouddirectory.types.string_attribute_value


class _TypedAttributeValue_StringValue(TypedDict):
    StringValue: (
        "aws_sdk_clouddirectory.types.string_attribute_value.StringAttributeValue"
    )


class _TypedAttributeValue_BinaryValue(TypedDict):
    BinaryValue: (
        "aws_sdk_clouddirectory.types.binary_attribute_value.BinaryAttributeValue"
    )


class _TypedAttributeValue_BooleanValue(TypedDict):
    BooleanValue: (
        "aws_sdk_clouddirectory.types.boolean_attribute_value.BooleanAttributeValue"
    )


class _TypedAttributeValue_NumberValue(TypedDict):
    NumberValue: (
        "aws_sdk_clouddirectory.types.number_attribute_value.NumberAttributeValue"
    )


class _TypedAttributeValue_DatetimeValue(TypedDict):
    DatetimeValue: (
        "aws_sdk_clouddirectory.types.datetime_attribute_value.DatetimeAttributeValue"
    )


TypedAttributeValue: TypeAlias = (
    _TypedAttributeValue_StringValue
    | _TypedAttributeValue_BinaryValue
    | _TypedAttributeValue_BooleanValue
    | _TypedAttributeValue_NumberValue
    | _TypedAttributeValue_DatetimeValue
)


# --- restJson1 ser/de ---
def serialize_json(value: TypedAttributeValue) -> dict:
    if "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "BinaryValue" in value:
        import aws_sdk_clouddirectory.types.binary_attribute_value

        return {
            "BinaryValue": aws_sdk_clouddirectory.types.binary_attribute_value.serialize_json(
                value["BinaryValue"]
            )
        }
    elif "BooleanValue" in value:
        return {"BooleanValue": value["BooleanValue"]}
    elif "NumberValue" in value:
        return {"NumberValue": value["NumberValue"]}
    elif "DatetimeValue" in value:
        import aws_sdk_clouddirectory.types.datetime_attribute_value

        return {
            "DatetimeValue": aws_sdk_clouddirectory.types.datetime_attribute_value.serialize_json(
                value["DatetimeValue"]
            )
        }
    else:
        raise SerializationError("TypedAttributeValue: no variant present")


def deserialize_json(data: dict) -> TypedAttributeValue:
    if "StringValue" in data:
        return {"StringValue": data["StringValue"]}
    elif "BinaryValue" in data:
        import aws_sdk_clouddirectory.types.binary_attribute_value

        return {
            "BinaryValue": aws_sdk_clouddirectory.types.binary_attribute_value.deserialize_json(
                data["BinaryValue"]
            )
        }
    elif "BooleanValue" in data:
        return {"BooleanValue": data["BooleanValue"]}
    elif "NumberValue" in data:
        return {"NumberValue": data["NumberValue"]}
    elif "DatetimeValue" in data:
        import aws_sdk_clouddirectory.types.datetime_attribute_value

        return {
            "DatetimeValue": aws_sdk_clouddirectory.types.datetime_attribute_value.deserialize_json(
                data["DatetimeValue"]
            )
        }
    else:
        raise DeserializationError("TypedAttributeValue: no recognized variant key")
