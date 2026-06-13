"""Generated from Smithy shape ``com.amazonaws.backup#CreateLogicallyAirGappedBackupVaultInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.long
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.tags


class CreateLogicallyAirGappedBackupVaultInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Logically air-gapped backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>"""
    backup_vault_tags: NotRequired["aws_sdk_backup.types.tags.Tags"]
    """<p>The tags to assign to the vault.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The ID of the creation request.</p> <p>This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    min_retention_days: "aws_sdk_backup.types.long.Long"
    """<p>This setting specifies the minimum retention period that the vault retains its recovery points.</p> <p>The minimum value accepted is 7 days.</p>"""
    max_retention_days: "aws_sdk_backup.types.long.Long"
    """<p>The maximum retention period that the vault retains its recovery points.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN of the customer-managed KMS key to use for encrypting the logically air-gapped backup vault. If not specified, the vault will be encrypted with an Amazon Web Services-owned key managed by Amazon Web Services Backup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLogicallyAirGappedBackupVaultInput) -> dict:
    out: dict = {}
    if "backup_vault_tags" in value:
        import aws_sdk_backup.types.tags

        out["BackupVaultTags"] = aws_sdk_backup.types.tags.serialize_json(
            value["backup_vault_tags"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    out["MinRetentionDays"] = value["min_retention_days"]
    out["MaxRetentionDays"] = value["max_retention_days"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateLogicallyAirGappedBackupVaultInput:
    out: CreateLogicallyAirGappedBackupVaultInput = {}  # type: ignore[typeddict-item]
    if "BackupVaultTags" in data:
        import aws_sdk_backup.types.tags

        out["backup_vault_tags"] = aws_sdk_backup.types.tags.deserialize_json(
            data["BackupVaultTags"]
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "MinRetentionDays" in data:
        out["min_retention_days"] = data["MinRetentionDays"]
    else:
        raise DeserializationError(
            "CreateLogicallyAirGappedBackupVaultInput.min_retention_days required"
        )
    if "MaxRetentionDays" in data:
        out["max_retention_days"] = data["MaxRetentionDays"]
    else:
        raise DeserializationError(
            "CreateLogicallyAirGappedBackupVaultInput.max_retention_days required"
        )
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
