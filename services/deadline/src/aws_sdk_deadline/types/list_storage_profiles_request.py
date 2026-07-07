"""Generated from Smithy shape ``com.amazonaws.deadline#ListStorageProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token


class ListStorageProfilesRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the storage profile.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStorageProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStorageProfilesRequest:
    out: ListStorageProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
