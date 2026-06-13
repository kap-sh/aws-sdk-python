"""Generated from Smithy shape ``com.amazonaws.backup#UpdateBackupPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_plan_input
    import aws_sdk_backup.types.string


class UpdateBackupPlanInput(TypedDict):
    backup_plan_id: "aws_sdk_backup.types.string.string"
    """<p>The ID of the backup plan.</p>"""
    backup_plan: "aws_sdk_backup.types.backup_plan_input.BackupPlanInput"
    """<p>The body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackupPlanInput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.backup_plan_input

    out["BackupPlan"] = aws_sdk_backup.types.backup_plan_input.serialize_json(
        value["backup_plan"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBackupPlanInput:
    out: UpdateBackupPlanInput = {}  # type: ignore[typeddict-item]
    if "BackupPlan" in data:
        import aws_sdk_backup.types.backup_plan_input

        out["backup_plan"] = aws_sdk_backup.types.backup_plan_input.deserialize_json(
            data["BackupPlan"]
        )
    else:
        raise DeserializationError("UpdateBackupPlanInput.backup_plan required")
    return out
