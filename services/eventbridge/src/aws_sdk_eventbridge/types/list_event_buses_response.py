"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListEventBusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_bus_list
    import aws_sdk_eventbridge.types.next_token


class ListEventBusesResponse(TypedDict, closed=True):
    event_buses: NotRequired["aws_sdk_eventbridge.types.event_bus_list.EventBusList"]
    """<p>This list of event buses.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventBusesResponse) -> dict:
    out: dict = {}
    if "event_buses" in value:
        import aws_sdk_eventbridge.types.event_bus_list

        out["EventBuses"] = (
            aws_sdk_eventbridge.types.event_bus_list.serialize_aws_json_1_1(
                value["event_buses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventBusesResponse:
    out: ListEventBusesResponse = {}  # type: ignore[typeddict-item]
    if "EventBuses" in data:
        import aws_sdk_eventbridge.types.event_bus_list

        out["event_buses"] = (
            aws_sdk_eventbridge.types.event_bus_list.deserialize_aws_json_1_1(
                data["EventBuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
