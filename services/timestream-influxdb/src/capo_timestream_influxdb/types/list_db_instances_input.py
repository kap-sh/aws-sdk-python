"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ListDbInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.next_token


class ListDbInstancesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_timestream_influxdb.types.next_token.NextToken"]
    """<p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>"""
    max_results: NotRequired["capo_timestream_influxdb.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbInstancesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbInstancesInput:
    out: ListDbInstancesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
