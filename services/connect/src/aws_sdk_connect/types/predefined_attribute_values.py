"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeValues``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute_string_values_list


class _PredefinedAttributeValues_StringList(TypedDict):
    StringList: "aws_sdk_connect.types.predefined_attribute_string_values_list.PredefinedAttributeStringValuesList"


PredefinedAttributeValues: TypeAlias = _PredefinedAttributeValues_StringList


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeValues) -> dict:
    if "StringList" in value:
        import aws_sdk_connect.types.predefined_attribute_string_values_list

        return {
            "StringList": aws_sdk_connect.types.predefined_attribute_string_values_list.serialize_json(
                value["StringList"]
            )
        }
    else:
        raise SerializationError("PredefinedAttributeValues: no variant present")


def deserialize_json(data: dict) -> PredefinedAttributeValues:
    if "StringList" in data:
        import aws_sdk_connect.types.predefined_attribute_string_values_list

        return {
            "StringList": aws_sdk_connect.types.predefined_attribute_string_values_list.deserialize_json(
                data["StringList"]
            )
        }
    else:
        raise DeserializationError(
            "PredefinedAttributeValues: no recognized variant key"
        )
