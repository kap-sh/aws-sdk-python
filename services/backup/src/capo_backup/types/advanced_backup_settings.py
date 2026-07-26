"""Generated from Smithy shape ``com.amazonaws.backup#AdvancedBackupSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.advanced_backup_setting

AdvancedBackupSettings: TypeAlias = list[
    "capo_backup.types.advanced_backup_setting.AdvancedBackupSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedBackupSettings) -> list:
    import capo_backup.types.advanced_backup_setting

    out: list = []
    for item in value:
        out.append(capo_backup.types.advanced_backup_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdvancedBackupSettings:
    import capo_backup.types.advanced_backup_setting

    out: AdvancedBackupSettings = []
    for item in data:
        out.append(capo_backup.types.advanced_backup_setting.deserialize_json(item))
    return out
