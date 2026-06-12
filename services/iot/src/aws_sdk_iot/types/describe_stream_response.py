"""Generated from Smithy shape ``com.amazonaws.iot#DescribeStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.stream_info


class DescribeStreamResponse(TypedDict):
    stream_info: NotRequired["aws_sdk_iot.types.stream_info.StreamInfo"]
    """<p>Information about the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamResponse) -> dict:
    out: dict = {}
    if "stream_info" in value:
        import aws_sdk_iot.types.stream_info

        out["streamInfo"] = aws_sdk_iot.types.stream_info.serialize_json(
            value["stream_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeStreamResponse:
    out: DescribeStreamResponse = {}  # type: ignore[typeddict-item]
    if "streamInfo" in data:
        import aws_sdk_iot.types.stream_info

        out["stream_info"] = aws_sdk_iot.types.stream_info.deserialize_json(
            data["streamInfo"]
        )
    return out
