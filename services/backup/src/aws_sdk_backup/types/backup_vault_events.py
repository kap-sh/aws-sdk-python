"""Generated from Smithy shape ``com.amazonaws.backup#BackupVaultEvents``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_event

BackupVaultEvents: TypeAlias = list["aws_sdk_backup.types.backup_vault_event.BackupVaultEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: BackupVaultEvents) -> list:
    import aws_sdk_backup.types.backup_vault_event
    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.backup_vault_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupVaultEvents:
    import aws_sdk_backup.types.backup_vault_event
    out: BackupVaultEvents = []
    for item in data:
        out.append(aws_sdk_backup.types.backup_vault_event.deserialize_json(item))
    return out