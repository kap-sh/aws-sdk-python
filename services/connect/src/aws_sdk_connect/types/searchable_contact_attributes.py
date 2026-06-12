"""Generated from Smithy shape ``com.amazonaws.connect#SearchableContactAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.search_contacts_match_type
    import aws_sdk_connect.types.searchable_contact_attributes_criteria_list


class SearchableContactAttributes(TypedDict):
    criteria: "aws_sdk_connect.types.searchable_contact_attributes_criteria_list.SearchableContactAttributesCriteriaList"
    """<p>The list of criteria based on user-defined contact attributes that are configured for contact search.</p>"""
    match_type: NotRequired[
        "aws_sdk_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining search criteria using multiple searchable contact attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableContactAttributes) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.searchable_contact_attributes_criteria_list

    out["Criteria"] = (
        aws_sdk_connect.types.searchable_contact_attributes_criteria_list.serialize_json(
            value["criteria"]
        )
    )
    if "match_type" in value:
        import aws_sdk_connect.types.search_contacts_match_type

        out["MatchType"] = (
            aws_sdk_connect.types.search_contacts_match_type.serialize_json(
                value["match_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchableContactAttributes:
    out: SearchableContactAttributes = {}  # type: ignore[typeddict-item]
    if "Criteria" in data:
        import aws_sdk_connect.types.searchable_contact_attributes_criteria_list

        out["criteria"] = (
            aws_sdk_connect.types.searchable_contact_attributes_criteria_list.deserialize_json(
                data["Criteria"]
            )
        )
    else:
        raise DeserializationError("SearchableContactAttributes.criteria required")
    if "MatchType" in data:
        import aws_sdk_connect.types.search_contacts_match_type

        out["match_type"] = (
            aws_sdk_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    return out
