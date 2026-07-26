"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListEventConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_configurations_list
    import capo_iot_wireless.types.next_token


class ListEventConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    event_configurations_list: NotRequired[
        "capo_iot_wireless.types.event_configurations_list.EventConfigurationsList"
    ]
    """<p>Event configurations of all events for a single resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "event_configurations_list" in value:
        import capo_iot_wireless.types.event_configurations_list

        out["EventConfigurationsList"] = (
            capo_iot_wireless.types.event_configurations_list.serialize_json(
                value["event_configurations_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEventConfigurationsResponse:
    out: ListEventConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EventConfigurationsList" in data:
        import capo_iot_wireless.types.event_configurations_list

        out["event_configurations_list"] = (
            capo_iot_wireless.types.event_configurations_list.deserialize_json(
                data["EventConfigurationsList"]
            )
        )
    return out
