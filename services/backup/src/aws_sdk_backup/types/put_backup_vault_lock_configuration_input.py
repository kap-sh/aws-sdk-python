"""Generated from Smithy shape ``com.amazonaws.backup#PutBackupVaultLockConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.long


class PutBackupVaultLockConfigurationInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The Backup Vault Lock configuration that specifies the name of the backup vault it protects.</p>"""
    min_retention_days: NotRequired["aws_sdk_backup.types.long.Long"]
    """<p>The Backup Vault Lock configuration that specifies the minimum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to retain certain data for at least seven years (2555 days).</p> <p>This parameter is required when a vault lock is created through CloudFormation; otherwise, this parameter is optional. If this parameter is not specified, Vault Lock will not enforce a minimum retention period.</p> <p>If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. The shortest minimum retention period you can specify is 1 day. Recovery points already saved in the vault prior to Vault Lock are not affected.</p>"""
    max_retention_days: NotRequired["aws_sdk_backup.types.long.Long"]
    """<p>The Backup Vault Lock configuration that specifies the maximum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to destroy certain data after retaining it for four years (1460 days).</p> <p>If this parameter is not included, Vault Lock does not enforce a maximum retention period on the recovery points in the vault. If this parameter is included without a value, Vault Lock will not enforce a maximum retention period.</p> <p>If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. The longest maximum retention period you can specify is 36500 days (approximately 100 years). Recovery points already saved in the vault prior to Vault Lock are not affected.</p>"""
    changeable_for_days: NotRequired["aws_sdk_backup.types.long.Long"]
    """<p>The Backup Vault Lock configuration that specifies the number of days before the lock date. For example, setting <code>ChangeableForDays</code> to 30 on Jan. 1, 2022 at 8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC.</p> <p>Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Therefore, you must set <code>ChangeableForDays</code> to 3 or greater.</p> <p>The maximum value you can specify is 36,500 days (approximately 100 years).</p> <p>Before the lock date, you can delete Vault Lock from the vault using <code>DeleteBackupVaultLockConfiguration</code> or change the Vault Lock configuration using <code>PutBackupVaultLockConfiguration</code>. On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted.</p> <p>If this parameter is not specified, you can delete Vault Lock from the vault using <code>DeleteBackupVaultLockConfiguration</code> or change the Vault Lock configuration using <code>PutBackupVaultLockConfiguration</code> at any time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBackupVaultLockConfigurationInput) -> dict:
    out: dict = {}
    if "min_retention_days" in value:
        out["MinRetentionDays"] = value["min_retention_days"]
    if "max_retention_days" in value:
        out["MaxRetentionDays"] = value["max_retention_days"]
    if "changeable_for_days" in value:
        out["ChangeableForDays"] = value["changeable_for_days"]
    return out


def deserialize_json(data: dict) -> PutBackupVaultLockConfigurationInput:
    out: PutBackupVaultLockConfigurationInput = {}  # type: ignore[typeddict-item]
    if "MinRetentionDays" in data:
        out["min_retention_days"] = data["MinRetentionDays"]
    if "MaxRetentionDays" in data:
        out["max_retention_days"] = data["MaxRetentionDays"]
    if "ChangeableForDays" in data:
        out["changeable_for_days"] = data["ChangeableForDays"]
    return out
