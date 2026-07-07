"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchQuickResponsesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.non_empty_string
    import aws_sdk_wisdom.types.quick_response_search_results_list


class SearchQuickResponsesResponse(TypedDict, closed=True):
    results: "aws_sdk_wisdom.types.quick_response_search_results_list.QuickResponseSearchResultsList"
    """<p>The results of the quick response search.</p>"""
    next_token: NotRequired["aws_sdk_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuickResponsesResponse) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.quick_response_search_results_list

    out["results"] = (
        aws_sdk_wisdom.types.quick_response_search_results_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchQuickResponsesResponse:
    out: SearchQuickResponsesResponse = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_wisdom.types.quick_response_search_results_list

        out["results"] = (
            aws_sdk_wisdom.types.quick_response_search_results_list.deserialize_json(
                data["results"]
            )
        )
    else:
        raise DeserializationError("SearchQuickResponsesResponse.results required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
