"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#AttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_directory_service_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.boolean_attribute_value
    import aws_sdk_directory_service_data.types.number_attribute_value
    import aws_sdk_directory_service_data.types.string_attribute_value
    import aws_sdk_directory_service_data.types.string_set_attribute_value


class _AttributeValue_S(TypedDict):
    S: "aws_sdk_directory_service_data.types.string_attribute_value.StringAttributeValue"


class _AttributeValue_N(TypedDict):
    N: "aws_sdk_directory_service_data.types.number_attribute_value.NumberAttributeValue"


class _AttributeValue_BOOL(TypedDict):
    BOOL: "aws_sdk_directory_service_data.types.boolean_attribute_value.BooleanAttributeValue"


class _AttributeValue_SS(TypedDict):
    SS: "aws_sdk_directory_service_data.types.string_set_attribute_value.StringSetAttributeValue"


AttributeValue: TypeAlias = (
    _AttributeValue_S | _AttributeValue_N | _AttributeValue_BOOL | _AttributeValue_SS
)


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValue) -> dict:
    if "S" in value:
        return {"S": value["S"]}
    elif "N" in value:
        return {"N": value["N"]}
    elif "BOOL" in value:
        return {"BOOL": value["BOOL"]}
    elif "SS" in value:
        import aws_sdk_directory_service_data.types.string_set_attribute_value

        return {
            "SS": aws_sdk_directory_service_data.types.string_set_attribute_value.serialize_json(
                value["SS"]
            )
        }
    else:
        raise SerializationError("AttributeValue: no variant present")


def deserialize_json(data: dict) -> AttributeValue:
    if "S" in data:
        return {"S": data["S"]}
    elif "N" in data:
        return {"N": data["N"]}
    elif "BOOL" in data:
        return {"BOOL": data["BOOL"]}
    elif "SS" in data:
        import aws_sdk_directory_service_data.types.string_set_attribute_value

        return {
            "SS": aws_sdk_directory_service_data.types.string_set_attribute_value.deserialize_json(
                data["SS"]
            )
        }
    else:
        raise DeserializationError("AttributeValue: no recognized variant key")
