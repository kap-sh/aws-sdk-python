"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupVaultAccessPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.iam_policy


class GetBackupVaultAccessPolicyOutput(TypedDict, closed=True):
    backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>"""
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    policy: NotRequired["capo_backup.types.iam_policy.IAMPolicy"]
    """<p>The backup vault access policy document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupVaultAccessPolicyOutput) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetBackupVaultAccessPolicyOutput:
    out: GetBackupVaultAccessPolicyOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
