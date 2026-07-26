"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeNotificationConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.notification_configuration


class DescribeNotificationConfigurationOutput(TypedDict, closed=True):
    notification_configuration: NotRequired[
        "capo_kinesis_video.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>The structure that contains the information required for notifications. If the structure is null, the configuration will be deleted from the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationConfigurationOutput) -> dict:
    out: dict = {}
    if "notification_configuration" in value:
        import capo_kinesis_video.types.notification_configuration

        out["NotificationConfiguration"] = (
            capo_kinesis_video.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeNotificationConfigurationOutput:
    out: DescribeNotificationConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "NotificationConfiguration" in data:
        import capo_kinesis_video.types.notification_configuration

        out["notification_configuration"] = (
            capo_kinesis_video.types.notification_configuration.deserialize_json(
                data["NotificationConfiguration"]
            )
        )
    return out
