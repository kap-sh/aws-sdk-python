"""Generated from Smithy shape ``com.amazonaws.backup#RestoreAccessBackupVaultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_access_backup_vault_list_member

RestoreAccessBackupVaultList: TypeAlias = list[
    "aws_sdk_backup.types.restore_access_backup_vault_list_member.RestoreAccessBackupVaultListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreAccessBackupVaultList) -> list:
    import aws_sdk_backup.types.restore_access_backup_vault_list_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup.types.restore_access_backup_vault_list_member.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RestoreAccessBackupVaultList:
    import aws_sdk_backup.types.restore_access_backup_vault_list_member

    out: RestoreAccessBackupVaultList = []
    for item in data:
        out.append(
            aws_sdk_backup.types.restore_access_backup_vault_list_member.deserialize_json(
                item
            )
        )
    return out
