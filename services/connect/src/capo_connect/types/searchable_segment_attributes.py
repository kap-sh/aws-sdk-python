"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_match_type
    import capo_connect.types.searchable_segment_attributes_criteria_list


class SearchableSegmentAttributes(TypedDict, closed=True):
    criteria: "capo_connect.types.searchable_segment_attributes_criteria_list.SearchableSegmentAttributesCriteriaList"
    """<p>The list of criteria based on searchable segment attributes.</p>"""
    match_type: NotRequired[
        "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining search criteria using multiple searchable segment attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributes) -> dict:
    out: dict = {}
    import capo_connect.types.searchable_segment_attributes_criteria_list

    out["Criteria"] = (
        capo_connect.types.searchable_segment_attributes_criteria_list.serialize_json(
            value["criteria"]
        )
    )
    if "match_type" in value:
        import capo_connect.types.search_contacts_match_type

        out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
            value["match_type"]
        )
    return out


def deserialize_json(data: dict) -> SearchableSegmentAttributes:
    out: SearchableSegmentAttributes = {}  # type: ignore[typeddict-item]
    if "Criteria" in data:
        import capo_connect.types.searchable_segment_attributes_criteria_list

        out["criteria"] = (
            capo_connect.types.searchable_segment_attributes_criteria_list.deserialize_json(
                data["Criteria"]
            )
        )
    else:
        raise DeserializationError("SearchableSegmentAttributes.criteria required")
    if "MatchType" in data:
        import capo_connect.types.search_contacts_match_type

        out["match_type"] = (
            capo_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    return out
