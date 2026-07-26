"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointByBackupVaultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.recovery_point_by_backup_vault

RecoveryPointByBackupVaultList: TypeAlias = list[
    "capo_backup.types.recovery_point_by_backup_vault.RecoveryPointByBackupVault"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointByBackupVaultList) -> list:
    import capo_backup.types.recovery_point_by_backup_vault

    out: list = []
    for item in value:
        out.append(
            capo_backup.types.recovery_point_by_backup_vault.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecoveryPointByBackupVaultList:
    import capo_backup.types.recovery_point_by_backup_vault

    out: RecoveryPointByBackupVaultList = []
    for item in data:
        out.append(
            capo_backup.types.recovery_point_by_backup_vault.deserialize_json(item)
        )
    return out
