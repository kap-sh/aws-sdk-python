"""Generated from Smithy shape ``com.amazonaws.connect#SearchableContactAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.searchable_contact_attribute_value

SearchableContactAttributeValueList: TypeAlias = list[
    "capo_connect.types.searchable_contact_attribute_value.SearchableContactAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableContactAttributeValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchableContactAttributeValueList:
    return list(data)
