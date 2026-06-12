"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#RemoveNotificationChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.notification_configuration


class RemoveNotificationChannelResponse(TypedDict):
    notification_configuration: NotRequired[
        "aws_sdk_codeguruprofiler.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>The new notification configuration for this profiling group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveNotificationChannelResponse) -> dict:
    out: dict = {}
    if "notification_configuration" in value:
        import aws_sdk_codeguruprofiler.types.notification_configuration

        out["notificationConfiguration"] = (
            aws_sdk_codeguruprofiler.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoveNotificationChannelResponse:
    out: RemoveNotificationChannelResponse = {}  # type: ignore[typeddict-item]
    if "notificationConfiguration" in data:
        import aws_sdk_codeguruprofiler.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_codeguruprofiler.types.notification_configuration.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    return out
