"""Generated from Smithy shape ``com.amazonaws.xray#PutTraceSegmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.unprocessed_trace_segment_list


class PutTraceSegmentsResult(TypedDict, closed=True):
    unprocessed_trace_segments: NotRequired[
        "aws_sdk_xray.types.unprocessed_trace_segment_list.UnprocessedTraceSegmentList"
    ]
    """<p>Segments that failed processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTraceSegmentsResult) -> dict:
    out: dict = {}
    if "unprocessed_trace_segments" in value:
        import aws_sdk_xray.types.unprocessed_trace_segment_list

        out["UnprocessedTraceSegments"] = (
            aws_sdk_xray.types.unprocessed_trace_segment_list.serialize_json(
                value["unprocessed_trace_segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutTraceSegmentsResult:
    out: PutTraceSegmentsResult = {}  # type: ignore[typeddict-item]
    if "UnprocessedTraceSegments" in data:
        import aws_sdk_xray.types.unprocessed_trace_segment_list

        out["unprocessed_trace_segments"] = (
            aws_sdk_xray.types.unprocessed_trace_segment_list.deserialize_json(
                data["UnprocessedTraceSegments"]
            )
        )
    return out
