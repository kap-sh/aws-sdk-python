"""Generated from Smithy shape ``com.amazonaws.backup#IndexedRecoveryPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.indexed_recovery_point

IndexedRecoveryPointList: TypeAlias = list[
    "capo_backup.types.indexed_recovery_point.IndexedRecoveryPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexedRecoveryPointList) -> list:
    import capo_backup.types.indexed_recovery_point

    out: list = []
    for item in value:
        out.append(capo_backup.types.indexed_recovery_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndexedRecoveryPointList:
    import capo_backup.types.indexed_recovery_point

    out: IndexedRecoveryPointList = []
    for item in data:
        out.append(capo_backup.types.indexed_recovery_point.deserialize_json(item))
    return out
