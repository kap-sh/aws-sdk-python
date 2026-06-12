"""Generated from Smithy shape ``com.amazonaws.fis#ListActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.list_actions_max_results
    import aws_sdk_fis.types.next_token


class ListActionsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_fis.types.list_actions_max_results.ListActionsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_fis.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListActionsRequest:
    out: ListActionsRequest = {}  # type: ignore[typeddict-item]
    return out
