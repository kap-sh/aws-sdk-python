"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupVaultDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_backup_backup_vault_notifications_details
    import capo_securityhub.types.non_empty_string


class AwsBackupBackupVaultDetails(TypedDict, closed=True):
    backup_vault_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault. </p>"""
    backup_vault_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the Amazon Web Services account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. </p>"""
    encryption_key_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The unique ARN associated with the server-side encryption key. You can specify a key to encrypt your backups from services that support full Backup management. If you don't specify a key, Backup creates an KMS key for you by default. </p>"""
    notifications: NotRequired[
        "capo_securityhub.types.aws_backup_backup_vault_notifications_details.AwsBackupBackupVaultNotificationsDetails"
    ]
    """<p>The Amazon SNS event notifications for the specified backup vault. </p>"""
    access_policy: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A resource-based policy that is used to manage access permissions on the target backup vault. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupVaultDetails) -> dict:
    out: dict = {}
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "notifications" in value:
        import capo_securityhub.types.aws_backup_backup_vault_notifications_details

        out["Notifications"] = (
            capo_securityhub.types.aws_backup_backup_vault_notifications_details.serialize_json(
                value["notifications"]
            )
        )
    if "access_policy" in value:
        out["AccessPolicy"] = value["access_policy"]
    return out


def deserialize_json(data: dict) -> AwsBackupBackupVaultDetails:
    out: AwsBackupBackupVaultDetails = {}  # type: ignore[typeddict-item]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "Notifications" in data:
        import capo_securityhub.types.aws_backup_backup_vault_notifications_details

        out["notifications"] = (
            capo_securityhub.types.aws_backup_backup_vault_notifications_details.deserialize_json(
                data["Notifications"]
            )
        )
    if "AccessPolicy" in data:
        out["access_policy"] = data["AccessPolicy"]
    return out
