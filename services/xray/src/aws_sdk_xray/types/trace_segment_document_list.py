"""Generated from Smithy shape ``com.amazonaws.xray#TraceSegmentDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.trace_segment_document

TraceSegmentDocumentList: TypeAlias = list[
    "aws_sdk_xray.types.trace_segment_document.TraceSegmentDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceSegmentDocumentList) -> list:
    return list(value)


def deserialize_json(data: list) -> TraceSegmentDocumentList:
    return list(data)
