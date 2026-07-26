"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.event_type


class CreateNotificationConfigurationResponse(TypedDict, closed=True):
    event_type: NotRequired["capo_iot_managed_integrations.types.event_type.EventType"]
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationConfigurationResponse) -> dict:
    out: dict = {}
    if "event_type" in value:
        import capo_iot_managed_integrations.types.event_type

        out["EventType"] = (
            capo_iot_managed_integrations.types.event_type.serialize_json(
                value["event_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateNotificationConfigurationResponse:
    out: CreateNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        import capo_iot_managed_integrations.types.event_type

        out["event_type"] = (
            capo_iot_managed_integrations.types.event_type.deserialize_json(
                data["EventType"]
            )
        )
    return out
