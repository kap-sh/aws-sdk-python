"""Generated from Smithy shape ``com.amazonaws.backup#ScanActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.scan_action

ScanActions: TypeAlias = list["capo_backup.types.scan_action.ScanAction"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanActions) -> list:
    import capo_backup.types.scan_action

    out: list = []
    for item in value:
        out.append(capo_backup.types.scan_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanActions:
    import capo_backup.types.scan_action

    out: ScanActions = []
    for item in data:
        out.append(capo_backup.types.scan_action.deserialize_json(item))
    return out
