"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class GetBackupPlanFromTemplateInput(TypedDict):
    backup_plan_template_id: "aws_sdk_backup.types.string.string"
    """<p>Uniquely identifies a stored backup plan template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromTemplateInput:
    out: GetBackupPlanFromTemplateInput = {}  # type: ignore[typeddict-item]
    return out
