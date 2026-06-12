"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListStreamsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.next_token
    import aws_sdk_kinesis_video.types.stream_info_list


class ListStreamsOutput(TypedDict):
    stream_info_list: NotRequired[
        "aws_sdk_kinesis_video.types.stream_info_list.StreamInfoList"
    ]
    """<p>An array of <code>StreamInfo</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>If the response is truncated, the call returns this element with a token. To get the next batch of streams, use this token in your next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsOutput) -> dict:
    out: dict = {}
    if "stream_info_list" in value:
        import aws_sdk_kinesis_video.types.stream_info_list

        out["StreamInfoList"] = (
            aws_sdk_kinesis_video.types.stream_info_list.serialize_json(
                value["stream_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamsOutput:
    out: ListStreamsOutput = {}  # type: ignore[typeddict-item]
    if "StreamInfoList" in data:
        import aws_sdk_kinesis_video.types.stream_info_list

        out["stream_info_list"] = (
            aws_sdk_kinesis_video.types.stream_info_list.deserialize_json(
                data["StreamInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
