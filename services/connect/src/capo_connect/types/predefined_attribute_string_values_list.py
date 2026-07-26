"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeStringValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_string_value

PredefinedAttributeStringValuesList: TypeAlias = list[
    "capo_connect.types.predefined_attribute_string_value.PredefinedAttributeStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeStringValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> PredefinedAttributeStringValuesList:
    return list(data)
