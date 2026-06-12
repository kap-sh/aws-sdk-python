"""Generated from Smithy shape ``com.amazonaws.xray#UnprocessedTraceSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.unprocessed_trace_segment

UnprocessedTraceSegmentList: TypeAlias = list[
    "aws_sdk_xray.types.unprocessed_trace_segment.UnprocessedTraceSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedTraceSegmentList) -> list:
    import aws_sdk_xray.types.unprocessed_trace_segment

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.unprocessed_trace_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnprocessedTraceSegmentList:
    import aws_sdk_xray.types.unprocessed_trace_segment

    out: UnprocessedTraceSegmentList = []
    for item in data:
        out.append(aws_sdk_xray.types.unprocessed_trace_segment.deserialize_json(item))
    return out
