"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_recovery_point_type

RestoreTestingRecoveryPointTypeList: TypeAlias = list[
    "capo_backup.types.restore_testing_recovery_point_type.RestoreTestingRecoveryPointType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingRecoveryPointTypeList) -> list:
    import capo_backup.types.restore_testing_recovery_point_type

    out: list = []
    for item in value:
        out.append(
            capo_backup.types.restore_testing_recovery_point_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RestoreTestingRecoveryPointTypeList:
    import capo_backup.types.restore_testing_recovery_point_type

    out: RestoreTestingRecoveryPointTypeList = []
    for item in data:
        out.append(
            capo_backup.types.restore_testing_recovery_point_type.deserialize_json(item)
        )
    return out
