"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeValues``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_string_values_list


class _PredefinedAttributeValues_StringList(TypedDict, closed=True):
    StringList: "capo_connect.types.predefined_attribute_string_values_list.PredefinedAttributeStringValuesList"


PredefinedAttributeValues: TypeAlias = _PredefinedAttributeValues_StringList


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeValues) -> dict:
    if "StringList" in value:
        import capo_connect.types.predefined_attribute_string_values_list

        return {
            "StringList": capo_connect.types.predefined_attribute_string_values_list.serialize_json(
                value["StringList"]
            )
        }
    else:
        raise SerializationError("PredefinedAttributeValues: no variant present")


def deserialize_json(data: dict) -> PredefinedAttributeValues:
    if "StringList" in data:
        import capo_connect.types.predefined_attribute_string_values_list

        return {
            "StringList": capo_connect.types.predefined_attribute_string_values_list.deserialize_json(
                data["StringList"]
            )
        }
    else:
        raise DeserializationError(
            "PredefinedAttributeValues: no recognized variant key"
        )
