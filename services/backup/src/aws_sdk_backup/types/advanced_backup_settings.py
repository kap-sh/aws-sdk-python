"""Generated from Smithy shape ``com.amazonaws.backup#AdvancedBackupSettings``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_backup.types.advanced_backup_setting

AdvancedBackupSettings: TypeAlias = list["aws_sdk_backup.types.advanced_backup_setting.AdvancedBackupSetting"]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedBackupSettings) -> list:
    import aws_sdk_backup.types.advanced_backup_setting
    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.advanced_backup_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdvancedBackupSettings:
    import aws_sdk_backup.types.advanced_backup_setting
    out: AdvancedBackupSettings = []
    for item in data:
        out.append(aws_sdk_backup.types.advanced_backup_setting.deserialize_json(item))
    return out