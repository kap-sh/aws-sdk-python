"""Generated from Smithy shape ``com.amazonaws.xray#Trace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_boolean
    import aws_sdk_xray.types.nullable_double
    import aws_sdk_xray.types.segment_list
    import aws_sdk_xray.types.trace_id


class Trace(TypedDict):
    id: NotRequired["aws_sdk_xray.types.trace_id.TraceId"]
    """<p>The unique identifier for the request that generated the trace's segments and subsegments.</p>"""
    duration: NotRequired["aws_sdk_xray.types.nullable_double.NullableDouble"]
    """<p>The length of time in seconds between the start time of the earliest segment that started and the end time of the last segment that completed.</p>"""
    limit_exceeded: NotRequired["aws_sdk_xray.types.nullable_boolean.NullableBoolean"]
    """<p>LimitExceeded is set to true when the trace has exceeded the <code>Trace document size</code> limit. For more information about this limit and other X-Ray limits and quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/xray.html\">Amazon Web Services X-Ray endpoints and quotas</a>.</p>"""
    segments: NotRequired["aws_sdk_xray.types.segment_list.SegmentList"]
    """<p>Segment documents for the segments and subsegments that comprise the trace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "limit_exceeded" in value:
        out["LimitExceeded"] = value["limit_exceeded"]
    if "segments" in value:
        import aws_sdk_xray.types.segment_list

        out["Segments"] = aws_sdk_xray.types.segment_list.serialize_json(
            value["segments"]
        )
    return out


def deserialize_json(data: dict) -> Trace:
    out: Trace = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "LimitExceeded" in data:
        out["limit_exceeded"] = data["LimitExceeded"]
    if "Segments" in data:
        import aws_sdk_xray.types.segment_list

        out["segments"] = aws_sdk_xray.types.segment_list.deserialize_json(
            data["Segments"]
        )
    return out
