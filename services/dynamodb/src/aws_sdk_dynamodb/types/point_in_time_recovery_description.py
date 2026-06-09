"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.point_in_time_recovery_status
    import aws_sdk_dynamodb.types.recovery_period_in_days


class PointInTimeRecoveryDescription(TypedDict):
    point_in_time_recovery_status: NotRequired[
        "aws_sdk_dynamodb.types.point_in_time_recovery_status.PointInTimeRecoveryStatus"
    ]
    """<p>The current state of point in time recovery:</p> <ul> <li> <p> <code>ENABLED</code> - Point in time recovery is enabled.</p> </li> <li> <p> <code>DISABLED</code> - Point in time recovery is disabled.</p> </li> </ul>"""
    recovery_period_in_days: NotRequired[
        "aws_sdk_dynamodb.types.recovery_period_in_days.RecoveryPeriodInDays"
    ]
    """<p>The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional.</p>"""
    earliest_restorable_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>Specifies the earliest point in time you can restore your table to. You can restore your table to any point in time during the last 35 days. </p>"""
    latest_restorable_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p> <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoveryDescription) -> dict:
    out: dict = {}
    if "point_in_time_recovery_status" in value:
        import aws_sdk_dynamodb.types.point_in_time_recovery_status

        out["PointInTimeRecoveryStatus"] = (
            aws_sdk_dynamodb.types.point_in_time_recovery_status.serialize_aws_json_1_0(
                value["point_in_time_recovery_status"]
            )
        )
    if "recovery_period_in_days" in value:
        out["RecoveryPeriodInDays"] = value["recovery_period_in_days"]
    if "earliest_restorable_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["EarliestRestorableDateTime"] = (
            aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
                value["earliest_restorable_date_time"]
            )
        )
    if "latest_restorable_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["LatestRestorableDateTime"] = (
            aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
                value["latest_restorable_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecoveryDescription:
    out: PointInTimeRecoveryDescription = {}  # type: ignore[typeddict-item]
    if "PointInTimeRecoveryStatus" in data:
        import aws_sdk_dynamodb.types.point_in_time_recovery_status

        out["point_in_time_recovery_status"] = (
            aws_sdk_dynamodb.types.point_in_time_recovery_status.deserialize_aws_json_1_0(
                data["PointInTimeRecoveryStatus"]
            )
        )
    if "RecoveryPeriodInDays" in data:
        out["recovery_period_in_days"] = data["RecoveryPeriodInDays"]
    if "EarliestRestorableDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["earliest_restorable_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["EarliestRestorableDateTime"]
            )
        )
    if "LatestRestorableDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["latest_restorable_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["LatestRestorableDateTime"]
            )
        )
    return out
