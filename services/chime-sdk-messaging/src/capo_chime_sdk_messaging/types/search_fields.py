"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.search_field

SearchFields: TypeAlias = list[
    "capo_chime_sdk_messaging.types.search_field.SearchField"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFields) -> list:
    import capo_chime_sdk_messaging.types.search_field

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_messaging.types.search_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchFields:
    import capo_chime_sdk_messaging.types.search_field

    out: SearchFields = []
    for item in data:
        out.append(capo_chime_sdk_messaging.types.search_field.deserialize_json(item))
    return out
