"""Generated from Smithy shape ``com.amazonaws.connect#Transcript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_match_type
    import capo_connect.types.transcript_criteria_list


class Transcript(TypedDict, closed=True):
    criteria: "capo_connect.types.transcript_criteria_list.TranscriptCriteriaList"
    """<p>The list of search criteria based on Contact Lens conversational analytics transcript.</p>"""
    match_type: NotRequired[
        "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining search criteria using multiple transcript criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transcript) -> dict:
    out: dict = {}
    import capo_connect.types.transcript_criteria_list

    out["Criteria"] = capo_connect.types.transcript_criteria_list.serialize_json(
        value["criteria"]
    )
    if "match_type" in value:
        import capo_connect.types.search_contacts_match_type

        out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
            value["match_type"]
        )
    return out


def deserialize_json(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if "Criteria" in data:
        import capo_connect.types.transcript_criteria_list

        out["criteria"] = capo_connect.types.transcript_criteria_list.deserialize_json(
            data["Criteria"]
        )
    else:
        raise DeserializationError("Transcript.criteria required")
    if "MatchType" in data:
        import capo_connect.types.search_contacts_match_type

        out["match_type"] = (
            capo_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    return out
