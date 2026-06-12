"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListCollectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.max_result
    import aws_sdk_migrationhubstrategy.types.next_token


class ListCollectorsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>"""
    max_results: NotRequired["aws_sdk_migrationhubstrategy.types.max_result.MaxResult"]
    """<p> The maximum number of items to include in the response. The maximum value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollectorsRequest:
    out: ListCollectorsRequest = {}  # type: ignore[typeddict-item]
    return out
