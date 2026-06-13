"""Generated from Smithy shape ``com.amazonaws.backup#GetRecoveryPointIndexDetailsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.index_status
    import aws_sdk_backup.types.long
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class GetRecoveryPointIndexDetailsOutput(TypedDict):
    recovery_point_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies the backup vault where the recovery point index is stored.</p> <p>For example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    source_resource_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.</p>"""
    index_creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup index was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    index_deletion_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup index was deleted, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    index_completion_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup index finished creation, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    index_status: NotRequired["aws_sdk_backup.types.index_status.IndexStatus"]
    """<p>This is the current status for the backup index associated with the specified recovery point.</p> <p>Statuses are: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>"""
    index_status_message: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A detailed message explaining the status of a backup index associated with the recovery point.</p>"""
    total_items_indexed: NotRequired["aws_sdk_backup.types.long.Long"]
    """<p>Count of items within the backup index associated with the recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPointIndexDetailsOutput) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    if "index_creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["IndexCreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["index_creation_date"]
        )
    if "index_deletion_date" in value:
        import aws_sdk_backup.types.timestamp

        out["IndexDeletionDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["index_deletion_date"]
        )
    if "index_completion_date" in value:
        import aws_sdk_backup.types.timestamp

        out["IndexCompletionDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["index_completion_date"]
        )
    if "index_status" in value:
        import aws_sdk_backup.types.index_status

        out["IndexStatus"] = aws_sdk_backup.types.index_status.serialize_json(
            value["index_status"]
        )
    if "index_status_message" in value:
        out["IndexStatusMessage"] = value["index_status_message"]
    if "total_items_indexed" in value:
        out["TotalItemsIndexed"] = value["total_items_indexed"]
    return out


def deserialize_json(data: dict) -> GetRecoveryPointIndexDetailsOutput:
    out: GetRecoveryPointIndexDetailsOutput = {}  # type: ignore[typeddict-item]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "SourceResourceArn" in data:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if "IndexCreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["index_creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["IndexCreationDate"]
        )
    if "IndexDeletionDate" in data:
        import aws_sdk_backup.types.timestamp

        out["index_deletion_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["IndexDeletionDate"]
        )
    if "IndexCompletionDate" in data:
        import aws_sdk_backup.types.timestamp

        out["index_completion_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["IndexCompletionDate"]
        )
    if "IndexStatus" in data:
        import aws_sdk_backup.types.index_status

        out["index_status"] = aws_sdk_backup.types.index_status.deserialize_json(
            data["IndexStatus"]
        )
    if "IndexStatusMessage" in data:
        out["index_status_message"] = data["IndexStatusMessage"]
    if "TotalItemsIndexed" in data:
        out["total_items_indexed"] = data["TotalItemsIndexed"]
    return out
