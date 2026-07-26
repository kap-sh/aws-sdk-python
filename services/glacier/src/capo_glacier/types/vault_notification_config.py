"""Generated from Smithy shape ``com.amazonaws.glacier#VaultNotificationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.notification_event_list
    import capo_glacier.types.string


class VaultNotificationConfig(TypedDict, closed=True):
    sns_topic: NotRequired["capo_glacier.types.string.string"]
    """<p>The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).</p>"""
    events: NotRequired[
        "capo_glacier.types.notification_event_list.NotificationEventList"
    ]
    """<p>A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VaultNotificationConfig) -> dict:
    out: dict = {}
    if "sns_topic" in value:
        out["SNSTopic"] = value["sns_topic"]
    if "events" in value:
        import capo_glacier.types.notification_event_list

        out["Events"] = capo_glacier.types.notification_event_list.serialize_json(
            value["events"]
        )
    return out


def deserialize_json(data: dict) -> VaultNotificationConfig:
    out: VaultNotificationConfig = {}  # type: ignore[typeddict-item]
    if "SNSTopic" in data:
        out["sns_topic"] = data["SNSTopic"]
    if "Events" in data:
        import capo_glacier.types.notification_event_list

        out["events"] = capo_glacier.types.notification_event_list.deserialize_json(
            data["Events"]
        )
    return out
