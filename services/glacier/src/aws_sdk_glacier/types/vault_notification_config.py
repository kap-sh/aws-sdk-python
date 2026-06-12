"""Generated from Smithy shape ``com.amazonaws.glacier#VaultNotificationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.notification_event_list
    import aws_sdk_glacier.types.string


class VaultNotificationConfig(TypedDict):
    sns_topic: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).</p>"""
    events: NotRequired[
        "aws_sdk_glacier.types.notification_event_list.NotificationEventList"
    ]
    """<p>A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VaultNotificationConfig) -> dict:
    out: dict = {}
    if "sns_topic" in value:
        out["SNSTopic"] = value["sns_topic"]
    if "events" in value:
        import aws_sdk_glacier.types.notification_event_list

        out["Events"] = aws_sdk_glacier.types.notification_event_list.serialize_json(
            value["events"]
        )
    return out


def deserialize_json(data: dict) -> VaultNotificationConfig:
    out: VaultNotificationConfig = {}  # type: ignore[typeddict-item]
    if "SNSTopic" in data:
        out["sns_topic"] = data["SNSTopic"]
    if "Events" in data:
        import aws_sdk_glacier.types.notification_event_list

        out["events"] = aws_sdk_glacier.types.notification_event_list.deserialize_json(
            data["Events"]
        )
    return out
