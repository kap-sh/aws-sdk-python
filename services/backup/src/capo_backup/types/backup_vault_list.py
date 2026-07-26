"""Generated from Smithy shape ``com.amazonaws.backup#BackupVaultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.backup_vault_list_member

BackupVaultList: TypeAlias = list[
    "capo_backup.types.backup_vault_list_member.BackupVaultListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupVaultList) -> list:
    import capo_backup.types.backup_vault_list_member

    out: list = []
    for item in value:
        out.append(capo_backup.types.backup_vault_list_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupVaultList:
    import capo_backup.types.backup_vault_list_member

    out: BackupVaultList = []
    for item in data:
        out.append(capo_backup.types.backup_vault_list_member.deserialize_json(item))
    return out
