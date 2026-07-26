"""Generated from Smithy shape ``com.amazonaws.wisdom#ListQuickResponsesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.quick_response_summary_list


class ListQuickResponsesResponse(TypedDict, closed=True):
    quick_response_summaries: (
        "capo_wisdom.types.quick_response_summary_list.QuickResponseSummaryList"
    )
    """<p>Summary information about the quick responses.</p>"""
    next_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuickResponsesResponse) -> dict:
    out: dict = {}
    import capo_wisdom.types.quick_response_summary_list

    out["quickResponseSummaries"] = (
        capo_wisdom.types.quick_response_summary_list.serialize_json(
            value["quick_response_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuickResponsesResponse:
    out: ListQuickResponsesResponse = {}  # type: ignore[typeddict-item]
    if "quickResponseSummaries" in data:
        import capo_wisdom.types.quick_response_summary_list

        out["quick_response_summaries"] = (
            capo_wisdom.types.quick_response_summary_list.deserialize_json(
                data["quickResponseSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListQuickResponsesResponse.quick_response_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
