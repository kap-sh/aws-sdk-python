"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListSignalingChannelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_info_list
    import aws_sdk_kinesis_video.types.next_token


class ListSignalingChannelsOutput(TypedDict, closed=True):
    channel_info_list: NotRequired[
        "aws_sdk_kinesis_video.types.channel_info_list.ChannelInfoList"
    ]
    """<p>An array of <code>ChannelInfo</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>If the response is truncated, the call returns this element with a token. To get the next batch of streams, use this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSignalingChannelsOutput) -> dict:
    out: dict = {}
    if "channel_info_list" in value:
        import aws_sdk_kinesis_video.types.channel_info_list

        out["ChannelInfoList"] = (
            aws_sdk_kinesis_video.types.channel_info_list.serialize_json(
                value["channel_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSignalingChannelsOutput:
    out: ListSignalingChannelsOutput = {}  # type: ignore[typeddict-item]
    if "ChannelInfoList" in data:
        import aws_sdk_kinesis_video.types.channel_info_list

        out["channel_info_list"] = (
            aws_sdk_kinesis_video.types.channel_info_list.deserialize_json(
                data["ChannelInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
