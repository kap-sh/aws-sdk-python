"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListStreamGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.max_results
    import aws_sdk_gameliftstreams.types.next_token


class ListStreamGroupsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_gameliftstreams.types.next_token.NextToken"]
    """<p>A token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>"""
    max_results: NotRequired["aws_sdk_gameliftstreams.types.max_results.MaxResults"]
    """<p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamGroupsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStreamGroupsInput:
    out: ListStreamGroupsInput = {}  # type: ignore[typeddict-item]
    return out
