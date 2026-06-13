"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRecoveryPointIndexSettingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.index
    import aws_sdk_backup.types.index_status


class UpdateRecoveryPointIndexSettingsOutput(TypedDict):
    backup_vault_name: NotRequired[
        "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>"""
    recovery_point_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    index_status: NotRequired["aws_sdk_backup.types.index_status.IndexStatus"]
    """<p>This is the current status for the backup index associated with the specified recovery point.</p> <p>Statuses are: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>"""
    index: NotRequired["aws_sdk_backup.types.index.Index"]
    """<p>Index can have 1 of 2 possible values, either <code>ENABLED</code> or <code>DISABLED</code>.</p> <p>A value of <code>ENABLED</code> means a backup index for an eligible <code>ACTIVE</code> recovery point has been created.</p> <p>A value of <code>DISABLED</code> means a backup index was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPointIndexSettingsOutput) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "index_status" in value:
        import aws_sdk_backup.types.index_status

        out["IndexStatus"] = aws_sdk_backup.types.index_status.serialize_json(
            value["index_status"]
        )
    if "index" in value:
        import aws_sdk_backup.types.index

        out["Index"] = aws_sdk_backup.types.index.serialize_json(value["index"])
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPointIndexSettingsOutput:
    out: UpdateRecoveryPointIndexSettingsOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "IndexStatus" in data:
        import aws_sdk_backup.types.index_status

        out["index_status"] = aws_sdk_backup.types.index_status.deserialize_json(
            data["IndexStatus"]
        )
    if "Index" in data:
        import aws_sdk_backup.types.index

        out["index"] = aws_sdk_backup.types.index.deserialize_json(data["Index"])
    return out
