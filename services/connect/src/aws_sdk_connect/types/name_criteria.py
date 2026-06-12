"""Generated from Smithy shape ``com.amazonaws.connect#NameCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.search_contacts_match_type
    import aws_sdk_connect.types.search_text_list


class NameCriteria(TypedDict):
    search_text: "aws_sdk_connect.types.search_text_list.SearchTextList"
    """<p>The words or phrases used to match the contact name.</p>"""
    match_type: (
        "aws_sdk_connect.types.search_contacts_match_type.SearchContactsMatchType"
    )
    """<p>The match type combining name search criteria using multiple search texts in a name criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NameCriteria) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.search_text_list

    out["SearchText"] = aws_sdk_connect.types.search_text_list.serialize_json(
        value["search_text"]
    )
    import aws_sdk_connect.types.search_contacts_match_type

    out["MatchType"] = aws_sdk_connect.types.search_contacts_match_type.serialize_json(
        value["match_type"]
    )
    return out


def deserialize_json(data: dict) -> NameCriteria:
    out: NameCriteria = {}  # type: ignore[typeddict-item]
    if "SearchText" in data:
        import aws_sdk_connect.types.search_text_list

        out["search_text"] = aws_sdk_connect.types.search_text_list.deserialize_json(
            data["SearchText"]
        )
    else:
        raise DeserializationError("NameCriteria.search_text required")
    if "MatchType" in data:
        import aws_sdk_connect.types.search_contacts_match_type

        out["match_type"] = (
            aws_sdk_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    else:
        raise DeserializationError("NameCriteria.match_type required")
    return out
