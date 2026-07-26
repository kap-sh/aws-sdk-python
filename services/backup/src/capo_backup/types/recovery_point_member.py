"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.resource_type


class RecoveryPointMember(TypedDict, closed=True):
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the parent (composite) recovery point.</p>"""
    resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a saved resource.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The Amazon Web Services resource type that is saved as a recovery point.</p>"""
    backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of the backup vault (the logical container in which backups are stored).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointMember) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    return out


def deserialize_json(data: dict) -> RecoveryPointMember:
    out: RecoveryPointMember = {}  # type: ignore[typeddict-item]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    return out
