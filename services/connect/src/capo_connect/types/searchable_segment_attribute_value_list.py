"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.searchable_segment_attribute_value

SearchableSegmentAttributeValueList: TypeAlias = list[
    "capo_connect.types.searchable_segment_attribute_value.SearchableSegmentAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributeValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchableSegmentAttributeValueList:
    return list(data)
