"""Generated from Smithy shape ``com.amazonaws.xray#RetrievedTrace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_double
    import aws_sdk_xray.types.span_list
    import aws_sdk_xray.types.trace_id


class RetrievedTrace(TypedDict, closed=True):
    id: NotRequired["aws_sdk_xray.types.trace_id.TraceId"]
    """<p> The unique identifier for the span. </p>"""
    duration: NotRequired["aws_sdk_xray.types.nullable_double.NullableDouble"]
    """<p> The length of time in seconds between the start time of the root span and the end time of the last span that completed. </p>"""
    spans: NotRequired["aws_sdk_xray.types.span_list.SpanList"]
    """<p> Spans that comprise the trace. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedTrace) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "spans" in value:
        import aws_sdk_xray.types.span_list

        out["Spans"] = aws_sdk_xray.types.span_list.serialize_json(value["spans"])
    return out


def deserialize_json(data: dict) -> RetrievedTrace:
    out: RetrievedTrace = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "Spans" in data:
        import aws_sdk_xray.types.span_list

        out["spans"] = aws_sdk_xray.types.span_list.deserialize_json(data["Spans"])
    return out
