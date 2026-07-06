"""Generated from Smithy shape ``com.amazonaws.backup#ExportBackupPlanTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class ExportBackupPlanTemplateOutput(TypedDict, closed=True):
    backup_plan_template_json: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The body of a backup plan template in JSON format.</p> <note> <p>This is a signed JSON document that cannot be modified before being passed to <code>GetBackupPlanFromJSON.</code> </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportBackupPlanTemplateOutput) -> dict:
    out: dict = {}
    if "backup_plan_template_json" in value:
        out["BackupPlanTemplateJson"] = value["backup_plan_template_json"]
    return out


def deserialize_json(data: dict) -> ExportBackupPlanTemplateOutput:
    out: ExportBackupPlanTemplateOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlanTemplateJson" in data:
        out["backup_plan_template_json"] = data["BackupPlanTemplateJson"]
    return out
