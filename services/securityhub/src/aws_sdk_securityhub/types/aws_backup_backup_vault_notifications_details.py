"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupVaultNotificationsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsBackupBackupVaultNotificationsDetails(TypedDict, closed=True):
    backup_vault_events: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>An array of events that indicate the status of jobs to back up resources to the backup vault. The following events are supported:</p> <ul> <li> <p> <code>BACKUP_JOB_STARTED | BACKUP_JOB_COMPLETED</code> </p> </li> <li> <p> <code>COPY_JOB_STARTED | COPY_JOB_SUCCESSFUL | COPY_JOB_FAILED</code> </p> </li> <li> <p> <code>RESTORE_JOB_STARTED | RESTORE_JOB_COMPLETED | RECOVERY_POINT_MODIFIED</code> </p> </li> <li> <p> <code>S3_BACKUP_OBJECT_FAILED | S3_RESTORE_OBJECT_FAILED</code> </p> </li> </ul>"""
    sns_topic_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the Amazon SNS topic for a backup vault's events. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupVaultNotificationsDetails) -> dict:
    out: dict = {}
    if "backup_vault_events" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["BackupVaultEvents"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["backup_vault_events"]
            )
        )
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    return out


def deserialize_json(data: dict) -> AwsBackupBackupVaultNotificationsDetails:
    out: AwsBackupBackupVaultNotificationsDetails = {}  # type: ignore[typeddict-item]
    if "BackupVaultEvents" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["backup_vault_events"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["BackupVaultEvents"]
            )
        )
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    return out
