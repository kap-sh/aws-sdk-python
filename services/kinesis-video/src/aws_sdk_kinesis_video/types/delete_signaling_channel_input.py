"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DeleteSignalingChannelInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.version


class DeleteSignalingChannelInput(TypedDict):
    channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel that you want to delete.</p>"""
    current_version: NotRequired["aws_sdk_kinesis_video.types.version.Version"]
    """<p>The current version of the signaling channel that you want to delete. You can obtain the current version by invoking the <code>DescribeSignalingChannel</code> or <code>ListSignalingChannels</code> API operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSignalingChannelInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    return out


def deserialize_json(data: dict) -> DeleteSignalingChannelInput:
    out: DeleteSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    else:
        raise DeserializationError("DeleteSignalingChannelInput.channel_arn required")
    if "CurrentVersion" in data:
        out["current_version"] = data["CurrentVersion"]
    return out
