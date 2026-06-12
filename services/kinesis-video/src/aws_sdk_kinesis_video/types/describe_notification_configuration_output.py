"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeNotificationConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.notification_configuration


class DescribeNotificationConfigurationOutput(TypedDict):
    notification_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>The structure that contains the information required for notifications. If the structure is null, the configuration will be deleted from the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationConfigurationOutput) -> dict:
    out: dict = {}
    if "notification_configuration" in value:
        import aws_sdk_kinesis_video.types.notification_configuration

        out["NotificationConfiguration"] = (
            aws_sdk_kinesis_video.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeNotificationConfigurationOutput:
    out: DescribeNotificationConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "NotificationConfiguration" in data:
        import aws_sdk_kinesis_video.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_kinesis_video.types.notification_configuration.deserialize_json(
                data["NotificationConfiguration"]
            )
        )
    return out
