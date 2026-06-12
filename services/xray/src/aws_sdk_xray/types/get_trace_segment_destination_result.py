"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceSegmentDestinationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.trace_segment_destination
    import aws_sdk_xray.types.trace_segment_destination_status


class GetTraceSegmentDestinationResult(TypedDict):
    destination: NotRequired[
        "aws_sdk_xray.types.trace_segment_destination.TraceSegmentDestination"
    ]
    """<p> Retrieves the current destination. </p>"""
    status: NotRequired[
        "aws_sdk_xray.types.trace_segment_destination_status.TraceSegmentDestinationStatus"
    ]
    """<p> Status of the retrieval. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceSegmentDestinationResult) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_xray.types.trace_segment_destination

        out["Destination"] = (
            aws_sdk_xray.types.trace_segment_destination.serialize_json(
                value["destination"]
            )
        )
    if "status" in value:
        import aws_sdk_xray.types.trace_segment_destination_status

        out["Status"] = (
            aws_sdk_xray.types.trace_segment_destination_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTraceSegmentDestinationResult:
    out: GetTraceSegmentDestinationResult = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        import aws_sdk_xray.types.trace_segment_destination

        out["destination"] = (
            aws_sdk_xray.types.trace_segment_destination.deserialize_json(
                data["Destination"]
            )
        )
    if "Status" in data:
        import aws_sdk_xray.types.trace_segment_destination_status

        out["status"] = (
            aws_sdk_xray.types.trace_segment_destination_status.deserialize_json(
                data["Status"]
            )
        )
    return out
