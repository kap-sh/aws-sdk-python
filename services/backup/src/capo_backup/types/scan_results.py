"""Generated from Smithy shape ``com.amazonaws.backup#ScanResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.scan_result

ScanResults: TypeAlias = list["capo_backup.types.scan_result.ScanResult"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResults) -> list:
    import capo_backup.types.scan_result

    out: list = []
    for item in value:
        out.append(capo_backup.types.scan_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanResults:
    import capo_backup.types.scan_result

    out: ScanResults = []
    for item in data:
        out.append(capo_backup.types.scan_result.deserialize_json(item))
    return out
