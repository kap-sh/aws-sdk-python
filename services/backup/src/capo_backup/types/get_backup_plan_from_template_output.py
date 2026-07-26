"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_plan


class GetBackupPlanFromTemplateOutput(TypedDict, closed=True):
    backup_plan_document: NotRequired["capo_backup.types.backup_plan.BackupPlan"]
    """<p>Returns the body of a backup plan based on the target template, including the name, rules, and backup vault of the plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromTemplateOutput) -> dict:
    out: dict = {}
    if "backup_plan_document" in value:
        import capo_backup.types.backup_plan

        out["BackupPlanDocument"] = capo_backup.types.backup_plan.serialize_json(
            value["backup_plan_document"]
        )
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromTemplateOutput:
    out: GetBackupPlanFromTemplateOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlanDocument" in data:
        import capo_backup.types.backup_plan

        out["backup_plan_document"] = capo_backup.types.backup_plan.deserialize_json(
            data["BackupPlanDocument"]
        )
    return out
