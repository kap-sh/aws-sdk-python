"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeSignalingChannelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_info


class DescribeSignalingChannelOutput(TypedDict):
    channel_info: NotRequired["aws_sdk_kinesis_video.types.channel_info.ChannelInfo"]
    """<p>A structure that encapsulates the specified signaling channel's metadata and properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSignalingChannelOutput) -> dict:
    out: dict = {}
    if "channel_info" in value:
        import aws_sdk_kinesis_video.types.channel_info

        out["ChannelInfo"] = aws_sdk_kinesis_video.types.channel_info.serialize_json(
            value["channel_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeSignalingChannelOutput:
    out: DescribeSignalingChannelOutput = {}  # type: ignore[typeddict-item]
    if "ChannelInfo" in data:
        import aws_sdk_kinesis_video.types.channel_info

        out["channel_info"] = aws_sdk_kinesis_video.types.channel_info.deserialize_json(
            data["ChannelInfo"]
        )
    return out
