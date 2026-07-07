"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeNotificationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name


class DescribeNotificationConfigurationInput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream from which to retrieve the notification configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to retrieve the notification configuration. You must specify either the <code>StreamName</code> or the StreamARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationConfigurationInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> DescribeNotificationConfigurationInput:
    out: DescribeNotificationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    return out
