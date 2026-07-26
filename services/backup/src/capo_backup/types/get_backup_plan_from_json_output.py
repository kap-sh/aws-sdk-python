"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromJSONOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_plan


class GetBackupPlanFromJSONOutput(TypedDict, closed=True):
    backup_plan: NotRequired["capo_backup.types.backup_plan.BackupPlan"]
    """<p>Specifies the body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromJSONOutput) -> dict:
    out: dict = {}
    if "backup_plan" in value:
        import capo_backup.types.backup_plan

        out["BackupPlan"] = capo_backup.types.backup_plan.serialize_json(
            value["backup_plan"]
        )
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromJSONOutput:
    out: GetBackupPlanFromJSONOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlan" in data:
        import capo_backup.types.backup_plan

        out["backup_plan"] = capo_backup.types.backup_plan.deserialize_json(
            data["BackupPlan"]
        )
    return out
