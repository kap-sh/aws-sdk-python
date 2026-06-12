"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeSignalingChannelInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_name
    import aws_sdk_kinesis_video.types.resource_arn


class DescribeSignalingChannelInput(TypedDict):
    channel_name: NotRequired["aws_sdk_kinesis_video.types.channel_name.ChannelName"]
    """<p>The name of the signaling channel that you want to describe.</p>"""
    channel_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The ARN of the signaling channel that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSignalingChannelInput) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "channel_arn" in value:
        out["ChannelARN"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> DescribeSignalingChannelInput:
    out: DescribeSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    return out
