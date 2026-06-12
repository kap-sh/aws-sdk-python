"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListEventConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_configurations_list
    import aws_sdk_iot_wireless.types.next_token


class ListEventConfigurationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    event_configurations_list: NotRequired[
        "aws_sdk_iot_wireless.types.event_configurations_list.EventConfigurationsList"
    ]
    """<p>Event configurations of all events for a single resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "event_configurations_list" in value:
        import aws_sdk_iot_wireless.types.event_configurations_list

        out["EventConfigurationsList"] = (
            aws_sdk_iot_wireless.types.event_configurations_list.serialize_json(
                value["event_configurations_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEventConfigurationsResponse:
    out: ListEventConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EventConfigurationsList" in data:
        import aws_sdk_iot_wireless.types.event_configurations_list

        out["event_configurations_list"] = (
            aws_sdk_iot_wireless.types.event_configurations_list.deserialize_json(
                data["EventConfigurationsList"]
            )
        )
    return out
