"""Generated from Smithy shape ``com.amazonaws.fis#ListTargetResourceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.list_target_resource_types_max_results
    import capo_fis.types.next_token


class ListTargetResourceTypesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_fis.types.list_target_resource_types_max_results.ListTargetResourceTypesMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetResourceTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetResourceTypesRequest:
    out: ListTargetResourceTypesRequest = {}  # type: ignore[typeddict-item]
    return out
