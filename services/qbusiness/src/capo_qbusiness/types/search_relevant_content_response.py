"""Generated from Smithy shape ``com.amazonaws.qbusiness#SearchRelevantContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.relevant_content_list


class SearchRelevantContentResponse(TypedDict, closed=True):
    relevant_content: NotRequired[
        "capo_qbusiness.types.relevant_content_list.RelevantContentList"
    ]
    """<p>The list of relevant content items found.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next set of results, if there are any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelevantContentResponse) -> dict:
    out: dict = {}
    if "relevant_content" in value:
        import capo_qbusiness.types.relevant_content_list

        out["relevantContent"] = (
            capo_qbusiness.types.relevant_content_list.serialize_json(
                value["relevant_content"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchRelevantContentResponse:
    out: SearchRelevantContentResponse = {}  # type: ignore[typeddict-item]
    if "relevantContent" in data:
        import capo_qbusiness.types.relevant_content_list

        out["relevant_content"] = (
            capo_qbusiness.types.relevant_content_list.deserialize_json(
                data["relevantContent"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
