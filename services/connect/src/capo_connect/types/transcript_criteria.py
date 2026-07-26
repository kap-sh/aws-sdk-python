"""Generated from Smithy shape ``com.amazonaws.connect#TranscriptCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.participant_role
    import capo_connect.types.search_contacts_match_type
    import capo_connect.types.search_text_list


class TranscriptCriteria(TypedDict, closed=True):
    participant_role: "capo_connect.types.participant_role.ParticipantRole"
    """<p>The participant role in a transcript</p>"""
    search_text: "capo_connect.types.search_text_list.SearchTextList"
    """<p>The words or phrases used to search within a transcript.</p>"""
    match_type: "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    """<p>The match type combining search criteria using multiple search texts in a transcript criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptCriteria) -> dict:
    out: dict = {}
    import capo_connect.types.participant_role

    out["ParticipantRole"] = capo_connect.types.participant_role.serialize_json(
        value["participant_role"]
    )
    import capo_connect.types.search_text_list

    out["SearchText"] = capo_connect.types.search_text_list.serialize_json(
        value["search_text"]
    )
    import capo_connect.types.search_contacts_match_type

    out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
        value["match_type"]
    )
    return out


def deserialize_json(data: dict) -> TranscriptCriteria:
    out: TranscriptCriteria = {}  # type: ignore[typeddict-item]
    if "ParticipantRole" in data:
        import capo_connect.types.participant_role

        out["participant_role"] = capo_connect.types.participant_role.deserialize_json(
            data["ParticipantRole"]
        )
    else:
        raise DeserializationError("TranscriptCriteria.participant_role required")
    if "SearchText" in data:
        import capo_connect.types.search_text_list

        out["search_text"] = capo_connect.types.search_text_list.deserialize_json(
            data["SearchText"]
        )
    else:
        raise DeserializationError("TranscriptCriteria.search_text required")
    if "MatchType" in data:
        import capo_connect.types.search_contacts_match_type

        out["match_type"] = (
            capo_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    else:
        raise DeserializationError("TranscriptCriteria.match_type required")
    return out
