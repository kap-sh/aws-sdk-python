"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#RemoveNotificationChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.notification_configuration


class RemoveNotificationChannelResponse(TypedDict, closed=True):
    notification_configuration: NotRequired[
        "capo_codeguruprofiler.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>The new notification configuration for this profiling group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveNotificationChannelResponse) -> dict:
    out: dict = {}
    if "notification_configuration" in value:
        import capo_codeguruprofiler.types.notification_configuration

        out["notificationConfiguration"] = (
            capo_codeguruprofiler.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoveNotificationChannelResponse:
    out: RemoveNotificationChannelResponse = {}  # type: ignore[typeddict-item]
    if "notificationConfiguration" in data:
        import capo_codeguruprofiler.types.notification_configuration

        out["notification_configuration"] = (
            capo_codeguruprofiler.types.notification_configuration.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    return out
