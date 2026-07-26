"""Generated from Smithy shape ``com.amazonaws.backup#BackupPlanTemplatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.backup_plan_templates_list_member

BackupPlanTemplatesList: TypeAlias = list[
    "capo_backup.types.backup_plan_templates_list_member.BackupPlanTemplatesListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupPlanTemplatesList) -> list:
    import capo_backup.types.backup_plan_templates_list_member

    out: list = []
    for item in value:
        out.append(
            capo_backup.types.backup_plan_templates_list_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BackupPlanTemplatesList:
    import capo_backup.types.backup_plan_templates_list_member

    out: BackupPlanTemplatesList = []
    for item in data:
        out.append(
            capo_backup.types.backup_plan_templates_list_member.deserialize_json(item)
        )
    return out
