"""Generated from Smithy shape ``com.amazonaws.ivs#StreamSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.boolean
    import aws_sdk_ivs.types.stream_id
    import aws_sdk_ivs.types.time


class StreamSessionSummary(TypedDict, closed=True):
    stream_id: NotRequired["aws_sdk_ivs.types.stream_id.StreamId"]
    """<p>Unique identifier for a live or previously live stream in the specified channel.</p>"""
    start_time: NotRequired["aws_sdk_ivs.types.time.Time"]
    """<p>Time when the channel went live. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    end_time: NotRequired["aws_sdk_ivs.types.time.Time"]
    """<p>Time when the channel went offline. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>. For live streams, this is <code>NULL</code>.</p>"""
    has_error_event: "aws_sdk_ivs.types.boolean.Boolean"
    """<p>If <code>true</code>, this stream encountered a quota breach or failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSessionSummary) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "start_time" in value:
        import aws_sdk_ivs.types.time

        out["startTime"] = aws_sdk_ivs.types.time.serialize_json(value["start_time"])
    if "end_time" in value:
        import aws_sdk_ivs.types.time

        out["endTime"] = aws_sdk_ivs.types.time.serialize_json(value["end_time"])
    out["hasErrorEvent"] = value.get("has_error_event", False)
    return out


def deserialize_json(data: dict) -> StreamSessionSummary:
    out: StreamSessionSummary = {}  # type: ignore[typeddict-item]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "startTime" in data:
        import aws_sdk_ivs.types.time

        out["start_time"] = aws_sdk_ivs.types.time.deserialize_json(data["startTime"])
    if "endTime" in data:
        import aws_sdk_ivs.types.time

        out["end_time"] = aws_sdk_ivs.types.time.deserialize_json(data["endTime"])
    if "hasErrorEvent" in data:
        out["has_error_event"] = data["hasErrorEvent"]
    else:
        out["has_error_event"] = False
    return out
