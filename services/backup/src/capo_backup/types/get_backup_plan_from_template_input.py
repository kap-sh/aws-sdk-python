"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string


class GetBackupPlanFromTemplateInput(TypedDict, closed=True):
    backup_plan_template_id: "capo_backup.types.string.string"
    """<p>Uniquely identifies a stored backup plan template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromTemplateInput:
    out: GetBackupPlanFromTemplateInput = {}  # type: ignore[typeddict-item]
    return out
