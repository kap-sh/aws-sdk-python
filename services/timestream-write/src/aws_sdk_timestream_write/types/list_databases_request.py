"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ListDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.pagination_limit
    import aws_sdk_timestream_write.types.string


class ListDatabasesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_timestream_write.types.string.String"]
    """<p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>"""
    max_results: NotRequired[
        "aws_sdk_timestream_write.types.pagination_limit.PaginationLimit"
    ]
    """<p>The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDatabasesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDatabasesRequest:
    out: ListDatabasesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
