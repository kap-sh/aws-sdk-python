"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchFieldValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.search_field_value

SearchFieldValues: TypeAlias = list[
    "capo_chime_sdk_messaging.types.search_field_value.SearchFieldValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFieldValues) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchFieldValues:
    return list(data)
