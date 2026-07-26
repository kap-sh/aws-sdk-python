"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.recovery_point_member

RecoveryPointsList: TypeAlias = list[
    "capo_backup.types.recovery_point_member.RecoveryPointMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointsList) -> list:
    import capo_backup.types.recovery_point_member

    out: list = []
    for item in value:
        out.append(capo_backup.types.recovery_point_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPointsList:
    import capo_backup.types.recovery_point_member

    out: RecoveryPointsList = []
    for item in data:
        out.append(capo_backup.types.recovery_point_member.deserialize_json(item))
    return out
