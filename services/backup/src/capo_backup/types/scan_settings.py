"""Generated from Smithy shape ``com.amazonaws.backup#ScanSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.scan_setting

ScanSettings: TypeAlias = list["capo_backup.types.scan_setting.ScanSetting"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanSettings) -> list:
    import capo_backup.types.scan_setting

    out: list = []
    for item in value:
        out.append(capo_backup.types.scan_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanSettings:
    import capo_backup.types.scan_setting

    out: ScanSettings = []
    for item in data:
        out.append(capo_backup.types.scan_setting.deserialize_json(item))
    return out
