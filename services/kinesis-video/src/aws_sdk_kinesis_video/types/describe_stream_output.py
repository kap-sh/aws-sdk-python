"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeStreamOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.stream_info


class DescribeStreamOutput(TypedDict):
    stream_info: NotRequired["aws_sdk_kinesis_video.types.stream_info.StreamInfo"]
    """<p>An object that describes the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamOutput) -> dict:
    out: dict = {}
    if "stream_info" in value:
        import aws_sdk_kinesis_video.types.stream_info

        out["StreamInfo"] = aws_sdk_kinesis_video.types.stream_info.serialize_json(
            value["stream_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeStreamOutput:
    out: DescribeStreamOutput = {}  # type: ignore[typeddict-item]
    if "StreamInfo" in data:
        import aws_sdk_kinesis_video.types.stream_info

        out["stream_info"] = aws_sdk_kinesis_video.types.stream_info.deserialize_json(
            data["StreamInfo"]
        )
    return out
