"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListEventBusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_bus_name
    import aws_sdk_eventbridge.types.limit_max100
    import aws_sdk_eventbridge.types.next_token


class ListEventBusesRequest(TypedDict, closed=True):
    name_prefix: NotRequired["aws_sdk_eventbridge.types.event_bus_name.EventBusName"]
    """<p>Specifying this limits the results to only those event buses with names that start with the specified prefix.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["aws_sdk_eventbridge.types.limit_max100.LimitMax100"]
    """<p>Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventBusesRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventBusesRequest:
    out: ListEventBusesRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
