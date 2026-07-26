"""Generated from Smithy shape ``com.amazonaws.backup#DescribeProtectedResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.long
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class DescribeProtectedResourceOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource saved as a recovery point; for example, an Amazon EBS volume or an Amazon RDS database.</p>"""
    last_backup_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastBackupTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    resource_name: NotRequired["capo_backup.types.string.string"]
    """<p>The name of the resource that belongs to the specified backup.</p>"""
    last_backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The ARN (Amazon Resource Name) of the backup vault that contains the most recent backup recovery point.</p>"""
    last_recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The ARN (Amazon Resource Name) of the most recent recovery point.</p>"""
    latest_restore_execution_time_minutes: NotRequired["capo_backup.types.long.Long"]
    """<p>The time, in minutes, that the most recent restore job took to complete.</p>"""
    latest_restore_job_creation_date: NotRequired[
        "capo_backup.types.timestamp.timestamp"
    ]
    """<p>The creation date of the most recent restore job.</p>"""
    latest_restore_recovery_point_creation_date: NotRequired[
        "capo_backup.types.timestamp.timestamp"
    ]
    """<p>The date the most recent recovery point was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProtectedResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "last_backup_time" in value:
        import capo_backup.types.timestamp

        out["LastBackupTime"] = capo_backup.types.timestamp.serialize_json(
            value["last_backup_time"]
        )
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "last_backup_vault_arn" in value:
        out["LastBackupVaultArn"] = value["last_backup_vault_arn"]
    if "last_recovery_point_arn" in value:
        out["LastRecoveryPointArn"] = value["last_recovery_point_arn"]
    if "latest_restore_execution_time_minutes" in value:
        out["LatestRestoreExecutionTimeMinutes"] = value[
            "latest_restore_execution_time_minutes"
        ]
    if "latest_restore_job_creation_date" in value:
        import capo_backup.types.timestamp

        out["LatestRestoreJobCreationDate"] = (
            capo_backup.types.timestamp.serialize_json(
                value["latest_restore_job_creation_date"]
            )
        )
    if "latest_restore_recovery_point_creation_date" in value:
        import capo_backup.types.timestamp

        out["LatestRestoreRecoveryPointCreationDate"] = (
            capo_backup.types.timestamp.serialize_json(
                value["latest_restore_recovery_point_creation_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeProtectedResourceOutput:
    out: DescribeProtectedResourceOutput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "LastBackupTime" in data:
        import capo_backup.types.timestamp

        out["last_backup_time"] = capo_backup.types.timestamp.deserialize_json(
            data["LastBackupTime"]
        )
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    if "LastBackupVaultArn" in data:
        out["last_backup_vault_arn"] = data["LastBackupVaultArn"]
    if "LastRecoveryPointArn" in data:
        out["last_recovery_point_arn"] = data["LastRecoveryPointArn"]
    if "LatestRestoreExecutionTimeMinutes" in data:
        out["latest_restore_execution_time_minutes"] = data[
            "LatestRestoreExecutionTimeMinutes"
        ]
    if "LatestRestoreJobCreationDate" in data:
        import capo_backup.types.timestamp

        out["latest_restore_job_creation_date"] = (
            capo_backup.types.timestamp.deserialize_json(
                data["LatestRestoreJobCreationDate"]
            )
        )
    if "LatestRestoreRecoveryPointCreationDate" in data:
        import capo_backup.types.timestamp

        out["latest_restore_recovery_point_creation_date"] = (
            capo_backup.types.timestamp.deserialize_json(
                data["LatestRestoreRecoveryPointCreationDate"]
            )
        )
    return out
