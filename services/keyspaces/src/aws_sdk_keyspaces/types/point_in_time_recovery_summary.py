"""Generated from Smithy shape ``com.amazonaws.keyspaces#PointInTimeRecoverySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.point_in_time_recovery_status
    import aws_sdk_keyspaces.types.timestamp


class PointInTimeRecoverySummary(TypedDict):
    status: "aws_sdk_keyspaces.types.point_in_time_recovery_status.PointInTimeRecoveryStatus"
    """<p>Shows if point-in-time recovery is enabled or disabled for the specified table.</p>"""
    earliest_restorable_timestamp: NotRequired[
        "aws_sdk_keyspaces.types.timestamp.Timestamp"
    ]
    """<p>Specifies the earliest possible restore point of the table in ISO 8601 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoverySummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "earliest_restorable_timestamp" in value:
        import aws_sdk_keyspaces.types.timestamp

        out["earliestRestorableTimestamp"] = (
            aws_sdk_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["earliest_restorable_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecoverySummary:
    out: PointInTimeRecoverySummary = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("PointInTimeRecoverySummary.status required")
    if "earliestRestorableTimestamp" in data:
        import aws_sdk_keyspaces.types.timestamp

        out["earliest_restorable_timestamp"] = (
            aws_sdk_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["earliestRestorableTimestamp"]
            )
        )
    return out
