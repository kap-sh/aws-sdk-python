"""Generated from Smithy shape ``com.amazonaws.iot#DescribeStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.stream_id


class DescribeStreamRequest(TypedDict):
    stream_id: "aws_sdk_iot.types.stream_id.StreamId"
    """<p>The stream ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeStreamRequest:
    out: DescribeStreamRequest = {}  # type: ignore[typeddict-item]
    return out
