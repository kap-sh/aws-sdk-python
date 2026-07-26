"""Generated from Smithy shape ``com.amazonaws.xray#UpdateTraceSegmentDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.trace_segment_destination


class UpdateTraceSegmentDestinationRequest(TypedDict, closed=True):
    destination: NotRequired[
        "capo_xray.types.trace_segment_destination.TraceSegmentDestination"
    ]
    """<p> The configured destination of trace segments. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTraceSegmentDestinationRequest) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_xray.types.trace_segment_destination

        out["Destination"] = capo_xray.types.trace_segment_destination.serialize_json(
            value["destination"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTraceSegmentDestinationRequest:
    out: UpdateTraceSegmentDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        import capo_xray.types.trace_segment_destination

        out["destination"] = capo_xray.types.trace_segment_destination.deserialize_json(
            data["Destination"]
        )
    return out
