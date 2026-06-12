"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateNotificationConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.notification_configuration
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name


class UpdateNotificationConfigurationInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream from which to update the notification configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to update the notification configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    notification_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>The structure containing the information required for notifications. If the structure is null, the configuration will be deleted from the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationConfigurationInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "notification_configuration" in value:
        import aws_sdk_kinesis_video.types.notification_configuration

        out["NotificationConfiguration"] = (
            aws_sdk_kinesis_video.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNotificationConfigurationInput:
    out: UpdateNotificationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "NotificationConfiguration" in data:
        import aws_sdk_kinesis_video.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_kinesis_video.types.notification_configuration.deserialize_json(
                data["NotificationConfiguration"]
            )
        )
    return out
