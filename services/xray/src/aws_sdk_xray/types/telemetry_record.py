"""Generated from Smithy shape ``com.amazonaws.xray#TelemetryRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.backend_connection_errors
    import aws_sdk_xray.types.nullable_integer
    import aws_sdk_xray.types.timestamp


class TelemetryRecord(TypedDict):
    timestamp: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p></p>"""
    segments_received_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_sent_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_spillover_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    segments_rejected_count: NotRequired[
        "aws_sdk_xray.types.nullable_integer.NullableInteger"
    ]
    """<p></p>"""
    backend_connection_errors: NotRequired[
        "aws_sdk_xray.types.backend_connection_errors.BackendConnectionErrors"
    ]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRecord) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.timestamp

    out["Timestamp"] = aws_sdk_xray.types.timestamp.serialize_json(value["timestamp"])
    if "segments_received_count" in value:
        out["SegmentsReceivedCount"] = value["segments_received_count"]
    if "segments_sent_count" in value:
        out["SegmentsSentCount"] = value["segments_sent_count"]
    if "segments_spillover_count" in value:
        out["SegmentsSpilloverCount"] = value["segments_spillover_count"]
    if "segments_rejected_count" in value:
        out["SegmentsRejectedCount"] = value["segments_rejected_count"]
    if "backend_connection_errors" in value:
        import aws_sdk_xray.types.backend_connection_errors

        out["BackendConnectionErrors"] = (
            aws_sdk_xray.types.backend_connection_errors.serialize_json(
                value["backend_connection_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryRecord:
    out: TelemetryRecord = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_xray.types.timestamp

        out["timestamp"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
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
        import aws_sdk_xray.types.backend_connection_errors

        out["backend_connection_errors"] = (
            aws_sdk_xray.types.backend_connection_errors.deserialize_json(
                data["BackendConnectionErrors"]
            )
        )
    return out
