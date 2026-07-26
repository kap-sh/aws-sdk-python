"""Generated from Smithy shape ``com.amazonaws.xray#TelemetryRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.backend_connection_errors
    import capo_xray.types.nullable_integer
    import capo_xray.types.timestamp


class TelemetryRecord(TypedDict, closed=True):
    timestamp: "capo_xray.types.timestamp.Timestamp"
    """<p></p>"""
    segments_received_count: NotRequired[
        "capo_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_sent_count: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p></p>"""
    segments_spillover_count: NotRequired[
        "capo_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_rejected_count: NotRequired[
        "capo_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    backend_connection_errors: NotRequired[
        "capo_xray.types.backend_connection_errors.BackendConnectionErrors"
    ]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRecord) -> dict:
    out: dict = {}
    import capo_xray.types.timestamp

    out["Timestamp"] = capo_xray.types.timestamp.serialize_json(value["timestamp"])
    if "segments_received_count" in value:
        out["SegmentsReceivedCount"] = value["segments_received_count"]
    if "segments_sent_count" in value:
        out["SegmentsSentCount"] = value["segments_sent_count"]
    if "segments_spillover_count" in value:
        out["SegmentsSpilloverCount"] = value["segments_spillover_count"]
    if "segments_rejected_count" in value:
        out["SegmentsRejectedCount"] = value["segments_rejected_count"]
    if "backend_connection_errors" in value:
        import capo_xray.types.backend_connection_errors

        out["BackendConnectionErrors"] = (
            capo_xray.types.backend_connection_errors.serialize_json(
                value["backend_connection_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryRecord:
    out: TelemetryRecord = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import capo_xray.types.timestamp

        out["timestamp"] = capo_xray.types.timestamp.deserialize_json(data["Timestamp"])
    else:
        raise DeserializationError("TelemetryRecord.timestamp required")
    if "SegmentsReceivedCount" in data:
        out["segments_received_count"] = data["SegmentsReceivedCount"]
    if "SegmentsSentCount" in data:
        out["segments_sent_count"] = data["SegmentsSentCount"]
    if "SegmentsSpilloverCount" in data:
        out["segments_spillover_count"] = data["SegmentsSpilloverCount"]
    if "SegmentsRejectedCount" in data:
        out["segments_rejected_count"] = data["SegmentsRejectedCount"]
    if "BackendConnectionErrors" in data:
        import capo_xray.types.backend_connection_errors

        out["backend_connection_errors"] = (
            capo_xray.types.backend_connection_errors.deserialize_json(
                data["BackendConnectionErrors"]
            )
        )
    return out
