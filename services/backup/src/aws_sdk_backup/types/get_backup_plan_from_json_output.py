"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromJSONOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_plan


class GetBackupPlanFromJSONOutput(TypedDict):
    backup_plan: NotRequired["aws_sdk_backup.types.backup_plan.BackupPlan"]
    """<p>Specifies the body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromJSONOutput) -> dict:
    out: dict = {}
    if "backup_plan" in value:
        import aws_sdk_backup.types.backup_plan

        out["BackupPlan"] = aws_sdk_backup.types.backup_plan.serialize_json(
            value["backup_plan"]
        )
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromJSONOutput:
    out: GetBackupPlanFromJSONOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlan" in data:
        import aws_sdk_backup.types.backup_plan

        out["backup_plan"] = aws_sdk_backup.types.backup_plan.deserialize_json(
            data["BackupPlan"]
        )
    return out
