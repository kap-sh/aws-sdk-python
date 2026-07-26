"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#NotificationConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.event_type


class NotificationConfigurationSummary(TypedDict, closed=True):
    event_type: NotRequired["capo_iot_managed_integrations.types.event_type.EventType"]
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""
    destination_name: NotRequired[
        "capo_iot_managed_integrations.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination for the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfigurationSummary) -> dict:
    out: dict = {}
    if "event_type" in value:
        import capo_iot_managed_integrations.types.event_type

        out["EventType"] = (
            capo_iot_managed_integrations.types.event_type.serialize_json(
                value["event_type"]
            )
        )
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    return out


def deserialize_json(data: dict) -> NotificationConfigurationSummary:
    out: NotificationConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        import capo_iot_managed_integrations.types.event_type

        out["event_type"] = (
            capo_iot_managed_integrations.types.event_type.deserialize_json(
                data["EventType"]
            )
        )
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    return out
