"""Generated from Smithy shape ``com.amazonaws.backup#BackupPlanTemplatesListMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class BackupPlanTemplatesListMember(TypedDict, closed=True):
    backup_plan_template_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Uniquely identifies a stored backup plan template.</p>"""
    backup_plan_template_name: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The optional display name of a backup plan template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupPlanTemplatesListMember) -> dict:
    out: dict = {}
    if "backup_plan_template_id" in value:
        out["BackupPlanTemplateId"] = value["backup_plan_template_id"]
    if "backup_plan_template_name" in value:
        out["BackupPlanTemplateName"] = value["backup_plan_template_name"]
    return out


def deserialize_json(data: dict) -> BackupPlanTemplatesListMember:
    out: BackupPlanTemplatesListMember = {}  # type: ignore[typeddict-item]
    if "BackupPlanTemplateId" in data:
        out["backup_plan_template_id"] = data["BackupPlanTemplateId"]
    if "BackupPlanTemplateName" in data:
        out["backup_plan_template_name"] = data["BackupPlanTemplateName"]
    return out
