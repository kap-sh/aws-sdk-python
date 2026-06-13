"""Generated from Smithy shape ``com.amazonaws.backup#GetRecoveryPointRestoreMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.metadata
    import aws_sdk_backup.types.resource_type


class GetRecoveryPointRestoreMetadataOutput(TypedDict):
    backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    recovery_point_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    restore_metadata: NotRequired["aws_sdk_backup.types.metadata.Metadata"]
    """<p>The set of metadata key-value pairs that describe the original configuration of the backed-up resource. These values vary depending on the service that is being restored.</p>"""
    resource_type: NotRequired["aws_sdk_backup.types.resource_type.ResourceType"]
    """<p>The resource type of the recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPointRestoreMetadataOutput) -> dict:
    out: dict = {}
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "restore_metadata" in value:
        import aws_sdk_backup.types.metadata

        out["RestoreMetadata"] = aws_sdk_backup.types.metadata.serialize_json(
            value["restore_metadata"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> GetRecoveryPointRestoreMetadataOutput:
    out: GetRecoveryPointRestoreMetadataOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "RestoreMetadata" in data:
        import aws_sdk_backup.types.metadata

        out["restore_metadata"] = aws_sdk_backup.types.metadata.deserialize_json(
            data["RestoreMetadata"]
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
