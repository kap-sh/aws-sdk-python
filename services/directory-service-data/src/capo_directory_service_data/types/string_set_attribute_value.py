"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#StringSetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service_data.types.string_attribute_value

StringSetAttributeValue: TypeAlias = list[
    "capo_directory_service_data.types.string_attribute_value.StringAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringSetAttributeValue) -> list:
    return list(value)


def deserialize_json(data: list) -> StringSetAttributeValue:
    return list(data)
