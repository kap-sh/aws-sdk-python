"""Generated from Smithy shape ``com.amazonaws.xray#UpdateTraceSegmentDestinationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.trace_segment_destination
    import capo_xray.types.trace_segment_destination_status


class UpdateTraceSegmentDestinationResult(TypedDict, closed=True):
    destination: NotRequired[
        "capo_xray.types.trace_segment_destination.TraceSegmentDestination"
    ]
    """<p> The destination of the trace segments. </p>"""
    status: NotRequired[
        "capo_xray.types.trace_segment_destination_status.TraceSegmentDestinationStatus"
    ]
    """<p> The status of the update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTraceSegmentDestinationResult) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_xray.types.trace_segment_destination

        out["Destination"] = capo_xray.types.trace_segment_destination.serialize_json(
            value["destination"]
        )
    if "status" in value:
        import capo_xray.types.trace_segment_destination_status

        out["Status"] = capo_xray.types.trace_segment_destination_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTraceSegmentDestinationResult:
    out: UpdateTraceSegmentDestinationResult = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        import capo_xray.types.trace_segment_destination

        out["destination"] = capo_xray.types.trace_segment_destination.deserialize_json(
            data["Destination"]
        )
    if "Status" in data:
        import capo_xray.types.trace_segment_destination_status

        out["status"] = (
            capo_xray.types.trace_segment_destination_status.deserialize_json(
                data["Status"]
            )
        )
    return out
