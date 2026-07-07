"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.autonomous_database_backup_status
    import aws_sdk_odb.types.autonomous_database_backup_type
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.resource_id


class AutonomousDatabaseBackup(TypedDict, closed=True):
    autonomous_database_backup_id: NotRequired[
        "aws_sdk_odb.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the Autonomous Database backup.</p>"""
    autonomous_database_backup_arn: NotRequired[
        "aws_sdk_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Autonomous Database backup.</p>"""
    autonomous_database_id: NotRequired["aws_sdk_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Autonomous Database that the backup was created from.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous Database backup.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database backup.</p>"""
    db_version: NotRequired["str"]
    """<p>The Oracle Database software version of the Autonomous Database backup.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
    ]
    """<p>The current status of the Autonomous Database backup.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database backup, if applicable.</p>"""
    is_automatic: NotRequired["bool"]
    """<p>Indicates whether the backup was created automatically.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for the Autonomous Database backup.</p>"""
    size_in_t_bs: NotRequired["float"]
    """<p>The size of the Autonomous Database backup, in terabytes (TB).</p>"""
    time_available_till: NotRequired["datetime.datetime"]
    """<p>The date and time until which the Autonomous Database backup is available for restore.</p>"""
    time_started: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database backup started.</p>"""
    time_ended: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database backup ended.</p>"""
    type: NotRequired[
        "aws_sdk_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
    ]
    """<p>The type of the Autonomous Database backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseBackup) -> dict:
    out: dict = {}
    if "autonomous_database_backup_id" in value:
        out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    if "autonomous_database_backup_arn" in value:
        out["autonomousDatabaseBackupArn"] = value["autonomous_database_backup_arn"]
    if "autonomous_database_id" in value:
        out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "db_version" in value:
        out["dbVersion"] = value["db_version"]
    if "status" in value:
        import aws_sdk_odb.types.autonomous_database_backup_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_backup_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "is_automatic" in value:
        out["isAutomatic"] = value["is_automatic"]
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    if "size_in_t_bs" in value:
        out["sizeInTBs"] = value["size_in_t_bs"]
    if "time_available_till" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeAvailableTill"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_available_till"]
            )
        )
    if "time_started" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeStarted"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_started"]
            )
        )
    if "time_ended" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeEnded"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["time_ended"]
        )
    if "type" in value:
        import aws_sdk_odb.types.autonomous_database_backup_type

        out["type"] = (
            aws_sdk_odb.types.autonomous_database_backup_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseBackup:
    out: AutonomousDatabaseBackup = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseBackupId" in data:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    if "autonomousDatabaseBackupArn" in data:
        out["autonomous_database_backup_arn"] = data["autonomousDatabaseBackupArn"]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "dbVersion" in data:
        out["db_version"] = data["dbVersion"]
    if "status" in data:
        import aws_sdk_odb.types.autonomous_database_backup_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_backup_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "isAutomatic" in data:
        out["is_automatic"] = data["isAutomatic"]
    if "retentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    if "sizeInTBs" in data:
        out["size_in_t_bs"] = data["sizeInTBs"]
    if "timeAvailableTill" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_available_till"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeAvailableTill"]
            )
        )
    if "timeStarted" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_started"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeStarted"]
            )
        )
    if "timeEnded" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_ended"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeEnded"]
            )
        )
    if "type" in data:
        import aws_sdk_odb.types.autonomous_database_backup_type

        out["type"] = (
            aws_sdk_odb.types.autonomous_database_backup_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    return out
