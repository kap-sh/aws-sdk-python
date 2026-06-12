"""Generated from Smithy shape ``com.amazonaws.connect#Transcript``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.search_contacts_match_type
    import aws_sdk_connect.types.transcript_criteria_list


class Transcript(TypedDict):
    criteria: "aws_sdk_connect.types.transcript_criteria_list.TranscriptCriteriaList"
    """<p>The list of search criteria based on Contact Lens conversational analytics transcript.</p>"""
    match_type: NotRequired[
        "aws_sdk_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining search criteria using multiple transcript criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transcript) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.transcript_criteria_list

    out["Criteria"] = aws_sdk_connect.types.transcript_criteria_list.serialize_json(
        value["criteria"]
    )
    if "match_type" in value:
        import aws_sdk_connect.types.search_contacts_match_type

        out["MatchType"] = (
            aws_sdk_connect.types.search_contacts_match_type.serialize_json(
                value["match_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if "Criteria" in data:
        import aws_sdk_connect.types.transcript_criteria_list

        out["criteria"] = (
            aws_sdk_connect.types.transcript_criteria_list.deserialize_json(
                data["Criteria"]
            )
        )
    else:
        raise DeserializationError("Transcript.criteria required")
    if "MatchType" in data:
        import aws_sdk_connect.types.search_contacts_match_type

        out["match_type"] = (
            aws_sdk_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    return out
