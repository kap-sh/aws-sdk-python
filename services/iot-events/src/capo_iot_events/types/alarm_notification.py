"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmNotification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.notification_actions


class AlarmNotification(TypedDict, closed=True):
    notification_actions: NotRequired[
        "capo_iot_events.types.notification_actions.NotificationActions"
    ]
    """<p>Contains the notification settings of an alarm model. The settings apply to all alarms that were created based on this alarm model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmNotification) -> dict:
    out: dict = {}
    if "notification_actions" in value:
        import capo_iot_events.types.notification_actions

        out["notificationActions"] = (
            capo_iot_events.types.notification_actions.serialize_json(
                value["notification_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AlarmNotification:
    out: AlarmNotification = {}  # type: ignore[typeddict-item]
    if "notificationActions" in data:
        import capo_iot_events.types.notification_actions

        out["notification_actions"] = (
            capo_iot_events.types.notification_actions.deserialize_json(
                data["notificationActions"]
            )
        )
    return out
