"""Generated from Smithy shape ``com.amazonaws.xray#PutTraceSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.trace_segment_document_list


class PutTraceSegmentsRequest(TypedDict, closed=True):
    trace_segment_documents: (
        "capo_xray.types.trace_segment_document_list.TraceSegmentDocumentList"
    )
    """<p>A string containing a JSON document defining one or more segments or subsegments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTraceSegmentsRequest) -> dict:
    out: dict = {}
    import capo_xray.types.trace_segment_document_list

    out["TraceSegmentDocuments"] = (
        capo_xray.types.trace_segment_document_list.serialize_json(
            value["trace_segment_documents"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTraceSegmentsRequest:
    out: PutTraceSegmentsRequest = {}  # type: ignore[typeddict-item]
    if "TraceSegmentDocuments" in data:
        import capo_xray.types.trace_segment_document_list

        out["trace_segment_documents"] = (
            capo_xray.types.trace_segment_document_list.deserialize_json(
                data["TraceSegmentDocuments"]
            )
        )
    else:
        raise DeserializationError(
            "PutTraceSegmentsRequest.trace_segment_documents required"
        )
    return out
