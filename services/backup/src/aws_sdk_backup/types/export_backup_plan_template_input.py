"""Generated from Smithy shape ``com.amazonaws.backup#ExportBackupPlanTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class ExportBackupPlanTemplateInput(TypedDict, closed=True):
    backup_plan_id: "aws_sdk_backup.types.string.string"
    """<p>Uniquely identifies a backup plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportBackupPlanTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportBackupPlanTemplateInput:
    out: ExportBackupPlanTemplateInput = {}  # type: ignore[typeddict-item]
    return out
