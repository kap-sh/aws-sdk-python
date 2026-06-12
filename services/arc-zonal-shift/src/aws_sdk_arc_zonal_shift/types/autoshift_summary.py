"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.autoshift_execution_status
    import aws_sdk_arc_zonal_shift.types.availability_zone
    import aws_sdk_arc_zonal_shift.types.expiry_time
    import aws_sdk_arc_zonal_shift.types.start_time


class AutoshiftSummary(TypedDict):
    away_from: "aws_sdk_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for a resource when Amazon Web Services starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the Amazon Web Services Region. An autoshift can end for a resource, for example, when Amazon Web Services ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.</p>"""
    end_time: NotRequired["aws_sdk_arc_zonal_shift.types.expiry_time.ExpiryTime"]
    """<p>The time (in UTC) when the autoshift ended.</p>"""
    start_time: "aws_sdk_arc_zonal_shift.types.start_time.StartTime"
    """<p>The time (in UTC) when the autoshift started.</p>"""
    status: "aws_sdk_arc_zonal_shift.types.autoshift_execution_status.AutoshiftExecutionStatus"
    """<p>The status for an autoshift. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftSummary) -> dict:
    out: dict = {}
    out["awayFrom"] = value["away_from"]
    if "end_time" in value:
        import aws_sdk_arc_zonal_shift.types.expiry_time

        out["endTime"] = aws_sdk_arc_zonal_shift.types.expiry_time.serialize_json(
            value["end_time"]
        )
    import aws_sdk_arc_zonal_shift.types.start_time

    out["startTime"] = aws_sdk_arc_zonal_shift.types.start_time.serialize_json(
        value["start_time"]
    )
    import aws_sdk_arc_zonal_shift.types.autoshift_execution_status

    out["status"] = (
        aws_sdk_arc_zonal_shift.types.autoshift_execution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutoshiftSummary:
    out: AutoshiftSummary = {}  # type: ignore[typeddict-item]
    if "awayFrom" in data:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("AutoshiftSummary.away_from required")
    if "endTime" in data:
        import aws_sdk_arc_zonal_shift.types.expiry_time

        out["end_time"] = aws_sdk_arc_zonal_shift.types.expiry_time.deserialize_json(
            data["endTime"]
        )
    if "startTime" in data:
        import aws_sdk_arc_zonal_shift.types.start_time

        out["start_time"] = aws_sdk_arc_zonal_shift.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("AutoshiftSummary.start_time required")
    if "status" in data:
        import aws_sdk_arc_zonal_shift.types.autoshift_execution_status

        out["status"] = (
            aws_sdk_arc_zonal_shift.types.autoshift_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AutoshiftSummary.status required")
    return out
