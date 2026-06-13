"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_plan


class GetBackupPlanFromTemplateOutput(TypedDict):
    backup_plan_document: NotRequired["aws_sdk_backup.types.backup_plan.BackupPlan"]
    """<p>Returns the body of a backup plan based on the target template, including the name, rules, and backup vault of the plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromTemplateOutput) -> dict:
    out: dict = {}
    if "backup_plan_document" in value:
        import aws_sdk_backup.types.backup_plan

        out["BackupPlanDocument"] = aws_sdk_backup.types.backup_plan.serialize_json(
            value["backup_plan_document"]
        )
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromTemplateOutput:
    out: GetBackupPlanFromTemplateOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlanDocument" in data:
        import aws_sdk_backup.types.backup_plan

        out["backup_plan_document"] = aws_sdk_backup.types.backup_plan.deserialize_json(
            data["BackupPlanDocument"]
        )
    return out
