"""Generated from Smithy shape ``com.amazonaws.deadline#ListLimitsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token


class ListLimitsRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the limits.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of limits to return in each page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLimitsRequest:
    out: ListLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
