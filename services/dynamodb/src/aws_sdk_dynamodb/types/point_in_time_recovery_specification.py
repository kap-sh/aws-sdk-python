"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoverySpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.boolean_object
    import aws_sdk_dynamodb.types.recovery_period_in_days


class PointInTimeRecoverySpecification(TypedDict):
    point_in_time_recovery_enabled: (
        "aws_sdk_dynamodb.types.boolean_object.BooleanObject"
    )
    """<p>Indicates whether point in time recovery is enabled (true) or disabled (false) on the table.</p>"""
    recovery_period_in_days: NotRequired[
        "aws_sdk_dynamodb.types.recovery_period_in_days.RecoveryPeriodInDays"
    ]
    """<p>The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional. If no value is provided, the value will default to 35.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoverySpecification) -> dict:
    out: dict = {}
    out["PointInTimeRecoveryEnabled"] = value["point_in_time_recovery_enabled"]
    if "recovery_period_in_days" in value:
        out["RecoveryPeriodInDays"] = value["recovery_period_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecoverySpecification:
    out: PointInTimeRecoverySpecification = {}  # type: ignore[typeddict-item]
    if "PointInTimeRecoveryEnabled" in data:
        out["point_in_time_recovery_enabled"] = data["PointInTimeRecoveryEnabled"]
    else:
        raise DeserializationError(
            "PointInTimeRecoverySpecification.point_in_time_recovery_enabled required"
        )
    if "RecoveryPeriodInDays" in data:
        out["recovery_period_in_days"] = data["RecoveryPeriodInDays"]
    return out
