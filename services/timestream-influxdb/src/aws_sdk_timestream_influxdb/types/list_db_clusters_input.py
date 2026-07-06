"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ListDbClustersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.max_results
    import aws_sdk_timestream_influxdb.types.next_token


class ListDbClustersInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_timestream_influxdb.types.next_token.NextToken"]
    """<p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>"""
    max_results: NotRequired["aws_sdk_timestream_influxdb.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbClustersInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbClustersInput:
    out: ListDbClustersInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
