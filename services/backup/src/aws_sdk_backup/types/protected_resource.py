"""Generated from Smithy shape ``com.amazonaws.backup#ProtectedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.resource_type
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class ProtectedResource(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    resource_type: NotRequired["aws_sdk_backup.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For Windows Volume Shadow Copy Service (VSS) backups, the only supported resource type is Amazon EC2.</p>"""
    last_backup_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastBackupTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    resource_name: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The non-unique name of the resource that belongs to the specified backup.</p>"""
    last_backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN (Amazon Resource Name) of the backup vault that contains the most recent backup recovery point.</p>"""
    last_recovery_point_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN (Amazon Resource Name) of the most recent recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedResource) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "last_backup_time" in value:
        import aws_sdk_backup.types.timestamp

        out["LastBackupTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["last_backup_time"]
        )
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "last_backup_vault_arn" in value:
        out["LastBackupVaultArn"] = value["last_backup_vault_arn"]
    if "last_recovery_point_arn" in value:
        out["LastRecoveryPointArn"] = value["last_recovery_point_arn"]
    return out


def deserialize_json(data: dict) -> ProtectedResource:
    out: ProtectedResource = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "LastBackupTime" in data:
        import aws_sdk_backup.types.timestamp

        out["last_backup_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["LastBackupTime"]
        )
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    if "LastBackupVaultArn" in data:
        out["last_backup_vault_arn"] = data["LastBackupVaultArn"]
    if "LastRecoveryPointArn" in data:
        out["last_recovery_point_arn"] = data["LastRecoveryPointArn"]
    return out
