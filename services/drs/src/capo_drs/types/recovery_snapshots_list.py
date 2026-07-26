"""Generated from Smithy shape ``com.amazonaws.drs#RecoverySnapshotsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_snapshot

RecoverySnapshotsList: TypeAlias = list[
    "capo_drs.types.recovery_snapshot.RecoverySnapshot"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoverySnapshotsList) -> list:
    import capo_drs.types.recovery_snapshot

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_snapshot.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoverySnapshotsList:
    import capo_drs.types.recovery_snapshot

    out: RecoverySnapshotsList = []
    for item in data:
        out.append(capo_drs.types.recovery_snapshot.deserialize_json(item))
    return out
