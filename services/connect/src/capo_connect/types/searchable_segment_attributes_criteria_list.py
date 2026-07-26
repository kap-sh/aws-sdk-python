"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributesCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.searchable_segment_attributes_criteria

SearchableSegmentAttributesCriteriaList: TypeAlias = list[
    "capo_connect.types.searchable_segment_attributes_criteria.SearchableSegmentAttributesCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributesCriteriaList) -> list:
    import capo_connect.types.searchable_segment_attributes_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.searchable_segment_attributes_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchableSegmentAttributesCriteriaList:
    import capo_connect.types.searchable_segment_attributes_criteria

    out: SearchableSegmentAttributesCriteriaList = []
    for item in data:
        out.append(
            capo_connect.types.searchable_segment_attributes_criteria.deserialize_json(
                item
            )
        )
    return out
