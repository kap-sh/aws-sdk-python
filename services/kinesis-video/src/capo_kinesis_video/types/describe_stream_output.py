"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.stream_info


class DescribeStreamOutput(TypedDict, closed=True):
    stream_info: NotRequired["capo_kinesis_video.types.stream_info.StreamInfo"]
    """<p>An object that describes the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamOutput) -> dict:
    out: dict = {}
    if "stream_info" in value:
        import capo_kinesis_video.types.stream_info

        out["StreamInfo"] = capo_kinesis_video.types.stream_info.serialize_json(
            value["stream_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeStreamOutput:
    out: DescribeStreamOutput = {}  # type: ignore[typeddict-item]
    if "StreamInfo" in data:
        import capo_kinesis_video.types.stream_info

        out["stream_info"] = capo_kinesis_video.types.stream_info.deserialize_json(
            data["StreamInfo"]
        )
    return out
