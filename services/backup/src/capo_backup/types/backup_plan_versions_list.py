"""Generated from Smithy shape ``com.amazonaws.backup#BackupPlanVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.backup_plans_list_member

BackupPlanVersionsList: TypeAlias = list[
    "capo_backup.types.backup_plans_list_member.BackupPlansListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupPlanVersionsList) -> list:
    import capo_backup.types.backup_plans_list_member

    out: list = []
    for item in value:
        out.append(capo_backup.types.backup_plans_list_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupPlanVersionsList:
    import capo_backup.types.backup_plans_list_member

    out: BackupPlanVersionsList = []
    for item in data:
        out.append(capo_backup.types.backup_plans_list_member.deserialize_json(item))
    return out
