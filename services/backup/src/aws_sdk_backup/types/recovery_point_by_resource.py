"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointByResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.aggregated_scan_result
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.boolean2
    import aws_sdk_backup.types.encryption_key_type
    import aws_sdk_backup.types.index_status
    import aws_sdk_backup.types.long
    import aws_sdk_backup.types.recovery_point_status
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp
    import aws_sdk_backup.types.vault_type


class RecoveryPointByResource(TypedDict, closed=True):
    recovery_point_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    status: NotRequired[
        "aws_sdk_backup.types.recovery_point_status.RecoveryPointStatus"
    ]
    """<p>A status code specifying the state of the recovery point.</p>"""
    status_message: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A message explaining the current status of the recovery point.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The server-side encryption key that is used to protect your backups; for example, <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p>"""
    backup_size_bytes: NotRequired["aws_sdk_backup.types.long.Long"]
    """<p>The size, in bytes, of a backup.</p>"""
    backup_vault_name: NotRequired[
        "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    is_parent: "aws_sdk_backup.types.boolean2.Boolean2"
    """<p>This is a boolean value indicating this is a parent (composite) recovery point.</p>"""
    parent_recovery_point_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the parent (composite) recovery point.</p>"""
    resource_name: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The non-unique name of the resource that belongs to the specified backup.</p>"""
    vault_type: NotRequired["aws_sdk_backup.types.vault_type.VaultType"]
    """<p>The type of vault in which the described recovery point is stored.</p>"""
    index_status: NotRequired["aws_sdk_backup.types.index_status.IndexStatus"]
    """<p>This is the current status for the backup index associated with the specified recovery point.</p> <p>Statuses are: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>"""
    index_status_message: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.</p>"""
    encryption_key_type: NotRequired[
        "aws_sdk_backup.types.encryption_key_type.EncryptionKeyType"
    ]
    """<p>The type of encryption key used for the recovery point. Valid values are CUSTOMER_MANAGED_KMS_KEY for customer-managed keys or Amazon Web Services_OWNED_KMS_KEY for Amazon Web Services-owned keys.</p>"""
    aggregated_scan_result: NotRequired[
        "aws_sdk_backup.types.aggregated_scan_result.AggregatedScanResult"
    ]
    """<p>Contains the latest scanning results against the recovery point and currently include <code>FailedScan</code>, <code>Findings</code>, <code>LastComputed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointByResource) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "status" in value:
        import aws_sdk_backup.types.recovery_point_status

        out["Status"] = aws_sdk_backup.types.recovery_point_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "backup_size_bytes" in value:
        out["BackupSizeBytes"] = value["backup_size_bytes"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    out["IsParent"] = value.get("is_parent", False)
    if "parent_recovery_point_arn" in value:
        out["ParentRecoveryPointArn"] = value["parent_recovery_point_arn"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "vault_type" in value:
        import aws_sdk_backup.types.vault_type

        out["VaultType"] = aws_sdk_backup.types.vault_type.serialize_json(
            value["vault_type"]
        )
    if "index_status" in value:
        import aws_sdk_backup.types.index_status

        out["IndexStatus"] = aws_sdk_backup.types.index_status.serialize_json(
            value["index_status"]
        )
    if "index_status_message" in value:
        out["IndexStatusMessage"] = value["index_status_message"]
    if "encryption_key_type" in value:
        import aws_sdk_backup.types.encryption_key_type

        out["EncryptionKeyType"] = (
            aws_sdk_backup.types.encryption_key_type.serialize_json(
                value["encryption_key_type"]
            )
        )
    if "aggregated_scan_result" in value:
        import aws_sdk_backup.types.aggregated_scan_result

        out["AggregatedScanResult"] = (
            aws_sdk_backup.types.aggregated_scan_result.serialize_json(
                value["aggregated_scan_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecoveryPointByResource:
    out: RecoveryPointByResource = {}  # type: ignore[typeddict-item]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "Status" in data:
        import aws_sdk_backup.types.recovery_point_status

        out["status"] = aws_sdk_backup.types.recovery_point_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "BackupSizeBytes" in data:
        out["backup_size_bytes"] = data["BackupSizeBytes"]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "IsParent" in data:
        out["is_parent"] = data["IsParent"]
    else:
        out["is_parent"] = False
    if "ParentRecoveryPointArn" in data:
        out["parent_recovery_point_arn"] = data["ParentRecoveryPointArn"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    if "VaultType" in data:
        import aws_sdk_backup.types.vault_type

        out["vault_type"] = aws_sdk_backup.types.vault_type.deserialize_json(
            data["VaultType"]
        )
    if "IndexStatus" in data:
        import aws_sdk_backup.types.index_status

        out["index_status"] = aws_sdk_backup.types.index_status.deserialize_json(
            data["IndexStatus"]
        )
    if "IndexStatusMessage" in data:
        out["index_status_message"] = data["IndexStatusMessage"]
    if "EncryptionKeyType" in data:
        import aws_sdk_backup.types.encryption_key_type

        out["encryption_key_type"] = (
            aws_sdk_backup.types.encryption_key_type.deserialize_json(
                data["EncryptionKeyType"]
            )
        )
    if "AggregatedScanResult" in data:
        import aws_sdk_backup.types.aggregated_scan_result

        out["aggregated_scan_result"] = (
            aws_sdk_backup.types.aggregated_scan_result.deserialize_json(
                data["AggregatedScanResult"]
            )
        )
    return out
