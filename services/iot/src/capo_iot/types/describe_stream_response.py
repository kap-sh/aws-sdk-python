"""Generated from Smithy shape ``com.amazonaws.iot#DescribeStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.stream_info


class DescribeStreamResponse(TypedDict, closed=True):
    stream_info: NotRequired["capo_iot.types.stream_info.StreamInfo"]
    """<p>Information about the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamResponse) -> dict:
    out: dict = {}
    if "stream_info" in value:
        import capo_iot.types.stream_info

        out["streamInfo"] = capo_iot.types.stream_info.serialize_json(
            value["stream_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeStreamResponse:
    out: DescribeStreamResponse = {}  # type: ignore[typeddict-item]
    if "streamInfo" in data:
        import capo_iot.types.stream_info

        out["stream_info"] = capo_iot.types.stream_info.deserialize_json(
            data["streamInfo"]
        )
    return out
