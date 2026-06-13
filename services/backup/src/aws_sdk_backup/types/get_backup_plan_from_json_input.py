"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromJSONInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class GetBackupPlanFromJSONInput(TypedDict):
    backup_plan_template_json: "aws_sdk_backup.types.string.string"
    """<p>A customer-supplied backup plan document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromJSONInput) -> dict:
    out: dict = {}
    out["BackupPlanTemplateJson"] = value["backup_plan_template_json"]
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromJSONInput:
    out: GetBackupPlanFromJSONInput = {}  # type: ignore[typeddict-item]
    if "BackupPlanTemplateJson" in data:
        out["backup_plan_template_json"] = data["BackupPlanTemplateJson"]
    else:
        raise DeserializationError(
            "GetBackupPlanFromJSONInput.backup_plan_template_json required"
        )
    return out
