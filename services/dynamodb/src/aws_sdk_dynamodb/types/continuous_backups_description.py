"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.continuous_backups_status
    import aws_sdk_dynamodb.types.point_in_time_recovery_description


class ContinuousBackupsDescription(TypedDict):
    continuous_backups_status: (
        "aws_sdk_dynamodb.types.continuous_backups_status.ContinuousBackupsStatus"
    )
    """<p> <code>ContinuousBackupsStatus</code> can be one of the following states: ENABLED, DISABLED</p>"""
    point_in_time_recovery_description: NotRequired[
        "aws_sdk_dynamodb.types.point_in_time_recovery_description.PointInTimeRecoveryDescription"
    ]
    """<p>The description of the point in time recovery settings applied to the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContinuousBackupsDescription) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.continuous_backups_status

    out["ContinuousBackupsStatus"] = (
        aws_sdk_dynamodb.types.continuous_backups_status.serialize_aws_json_1_0(
            value["continuous_backups_status"]
        )
    )
    if "point_in_time_recovery_description" in value:
        import aws_sdk_dynamodb.types.point_in_time_recovery_description

        out["PointInTimeRecoveryDescription"] = (
            aws_sdk_dynamodb.types.point_in_time_recovery_description.serialize_aws_json_1_0(
                value["point_in_time_recovery_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContinuousBackupsDescription:
    out: ContinuousBackupsDescription = {}  # type: ignore[typeddict-item]
    if "ContinuousBackupsStatus" in data:
        import aws_sdk_dynamodb.types.continuous_backups_status

        out["continuous_backups_status"] = (
            aws_sdk_dynamodb.types.continuous_backups_status.deserialize_aws_json_1_0(
                data["ContinuousBackupsStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ContinuousBackupsDescription.continuous_backups_status required"
        )
    if "PointInTimeRecoveryDescription" in data:
        import aws_sdk_dynamodb.types.point_in_time_recovery_description

        out["point_in_time_recovery_description"] = (
            aws_sdk_dynamodb.types.point_in_time_recovery_description.deserialize_aws_json_1_0(
                data["PointInTimeRecoveryDescription"]
            )
        )
    return out
