"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.event_type


class UpdateNotificationConfigurationRequest(TypedDict, closed=True):
    event_type: "capo_iot_managed_integrations.types.event_type.EventType"
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""
    destination_name: (
        "capo_iot_managed_integrations.types.destination_name.DestinationName"
    )
    """<p>The name of the destination for the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationConfigurationRequest) -> dict:
    out: dict = {}
    out["DestinationName"] = value["destination_name"]
    return out


def deserialize_json(data: dict) -> UpdateNotificationConfigurationRequest:
    out: UpdateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    else:
        raise DeserializationError(
            "UpdateNotificationConfigurationRequest.destination_name required"
        )
    return out
