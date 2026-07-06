"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupVaultNotificationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_events
    import aws_sdk_backup.types.backup_vault_name


class GetBackupVaultNotificationsOutput(TypedDict, closed=True):
    backup_vault_name: NotRequired[
        "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>"""
    backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic; for example, <code>arn:aws:sns:us-west-2:111122223333:MyTopic</code>.</p>"""
    backup_vault_events: NotRequired[
        "aws_sdk_backup.types.backup_vault_events.BackupVaultEvents"
    ]
    """<p>An array of events that indicate the status of jobs to back up resources to the backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupVaultNotificationsOutput) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "sns_topic_arn" in value:
        out["SNSTopicArn"] = value["sns_topic_arn"]
    if "backup_vault_events" in value:
        import aws_sdk_backup.types.backup_vault_events

        out["BackupVaultEvents"] = (
            aws_sdk_backup.types.backup_vault_events.serialize_json(
                value["backup_vault_events"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBackupVaultNotificationsOutput:
    out: GetBackupVaultNotificationsOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "SNSTopicArn" in data:
        out["sns_topic_arn"] = data["SNSTopicArn"]
    if "BackupVaultEvents" in data:
        import aws_sdk_backup.types.backup_vault_events

        out["backup_vault_events"] = (
            aws_sdk_backup.types.backup_vault_events.deserialize_json(
                data["BackupVaultEvents"]
            )
        )
    return out
