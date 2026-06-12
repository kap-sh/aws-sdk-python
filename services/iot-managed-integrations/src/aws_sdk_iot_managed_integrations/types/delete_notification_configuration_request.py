"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.event_type


class DeleteNotificationConfigurationRequest(TypedDict):
    event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType"
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotificationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotificationConfigurationRequest:
    out: DeleteNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
