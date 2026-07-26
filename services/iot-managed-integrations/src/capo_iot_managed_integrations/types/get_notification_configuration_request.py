"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.event_type


class GetNotificationConfigurationRequest(TypedDict, closed=True):
    event_type: "capo_iot_managed_integrations.types.event_type.EventType"
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationRequest:
    out: GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
