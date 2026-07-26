"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeMediaStorageConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.channel_name
    import capo_kinesis_video.types.resource_arn


class DescribeMediaStorageConfigurationInput(TypedDict, closed=True):
    channel_name: NotRequired["capo_kinesis_video.types.channel_name.ChannelName"]
    """<p>The name of the channel.</p>"""
    channel_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMediaStorageConfigurationInput) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "channel_arn" in value:
        out["ChannelARN"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> DescribeMediaStorageConfigurationInput:
    out: DescribeMediaStorageConfigurationInput = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    return out
