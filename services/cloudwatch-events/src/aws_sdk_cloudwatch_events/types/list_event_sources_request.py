"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListEventSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_source_name_prefix
    import aws_sdk_cloudwatch_events.types.limit_max100
    import aws_sdk_cloudwatch_events.types.next_token


class ListEventSourcesRequest(TypedDict, closed=True):
    name_prefix: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_source_name_prefix.EventSourceNamePrefix"
    ]
    """<p>Specifying this limits the results to only those partner event sources with names that start with the specified prefix.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"]
    """<p>Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventSourcesRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventSourcesRequest:
    out: ListEventSourcesRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
