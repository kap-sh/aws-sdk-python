"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListEventBusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_list
    import capo_cloudwatch_events.types.next_token


class ListEventBusesResponse(TypedDict, closed=True):
    event_buses: NotRequired["capo_cloudwatch_events.types.event_bus_list.EventBusList"]
    """<p>This list of event buses.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>A token you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventBusesResponse) -> dict:
    out: dict = {}
    if "event_buses" in value:
        import capo_cloudwatch_events.types.event_bus_list

        out["EventBuses"] = (
            capo_cloudwatch_events.types.event_bus_list.serialize_aws_json_1_1(
                value["event_buses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventBusesResponse:
    out: ListEventBusesResponse = {}  # type: ignore[typeddict-item]
    if "EventBuses" in data:
        import capo_cloudwatch_events.types.event_bus_list

        out["event_buses"] = (
            capo_cloudwatch_events.types.event_bus_list.deserialize_aws_json_1_1(
                data["EventBuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
