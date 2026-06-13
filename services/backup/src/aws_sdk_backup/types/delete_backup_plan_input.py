"""Generated from Smithy shape ``com.amazonaws.backup#DeleteBackupPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class DeleteBackupPlanInput(TypedDict):
    backup_plan_id: "aws_sdk_backup.types.string.string"
    """<p>Uniquely identifies a backup plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackupPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackupPlanInput:
    out: DeleteBackupPlanInput = {}  # type: ignore[typeddict-item]
    return out
