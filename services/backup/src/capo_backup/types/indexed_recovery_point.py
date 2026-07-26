"""Generated from Smithy shape ``com.amazonaws.backup#IndexedRecoveryPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.index_status
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class IndexedRecoveryPoint(TypedDict, closed=True):
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code> </p>"""
    source_resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.</p>"""
    iam_role_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>This specifies the IAM role ARN used for this operation.</p> <p>For example, arn:aws:iam::123456789012:role/S3Access</p>"""
    backup_creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The resource type of the indexed recovery point.</p> <ul> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul>"""
    index_creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup index was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    index_status: NotRequired["capo_backup.types.index_status.IndexStatus"]
    """<p>This is the current status for the backup index associated with the specified recovery point.</p> <p>Statuses are: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>"""
    index_status_message: NotRequired["capo_backup.types.string.string"]
    """<p>A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.</p>"""
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies the backup vault where the recovery point index is stored.</p> <p>For example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexedRecoveryPoint) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "backup_creation_date" in value:
        import capo_backup.types.timestamp

        out["BackupCreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["backup_creation_date"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "index_creation_date" in value:
        import capo_backup.types.timestamp

        out["IndexCreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["index_creation_date"]
        )
    if "index_status" in value:
        import capo_backup.types.index_status

        out["IndexStatus"] = capo_backup.types.index_status.serialize_json(
            value["index_status"]
        )
    if "index_status_message" in value:
        out["IndexStatusMessage"] = value["index_status_message"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    return out


def deserialize_json(data: dict) -> IndexedRecoveryPoint:
    out: IndexedRecoveryPoint = {}  # type: ignore[typeddict-item]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "SourceResourceArn" in data:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "BackupCreationDate" in data:
        import capo_backup.types.timestamp

        out["backup_creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["BackupCreationDate"]
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "IndexCreationDate" in data:
        import capo_backup.types.timestamp

        out["index_creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["IndexCreationDate"]
        )
    if "IndexStatus" in data:
        import capo_backup.types.index_status

        out["index_status"] = capo_backup.types.index_status.deserialize_json(
            data["IndexStatus"]
        )
    if "IndexStatusMessage" in data:
        out["index_status_message"] = data["IndexStatusMessage"]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    return out
