"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.content_summary_list
    import capo_wisdom.types.next_token


class SearchContentResponse(TypedDict, closed=True):
    content_summaries: "capo_wisdom.types.content_summary_list.ContentSummaryList"
    """<p>Summary information about the content.</p>"""
    next_token: NotRequired["capo_wisdom.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContentResponse) -> dict:
    out: dict = {}
    import capo_wisdom.types.content_summary_list

    out["contentSummaries"] = capo_wisdom.types.content_summary_list.serialize_json(
        value["content_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchContentResponse:
    out: SearchContentResponse = {}  # type: ignore[typeddict-item]
    if "contentSummaries" in data:
        import capo_wisdom.types.content_summary_list

        out["content_summaries"] = (
            capo_wisdom.types.content_summary_list.deserialize_json(
                data["contentSummaries"]
            )
        )
    else:
        raise DeserializationError("SearchContentResponse.content_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
