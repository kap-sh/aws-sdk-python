"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupSelectionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class GetBackupSelectionInput(TypedDict):
    backup_plan_id: "aws_sdk_backup.types.string.string"
    """<p>Uniquely identifies a backup plan.</p>"""
    selection_id: "aws_sdk_backup.types.string.string"
    """<p>Uniquely identifies the body of a request to assign a set of resources to a backup plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupSelectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupSelectionInput:
    out: GetBackupSelectionInput = {}  # type: ignore[typeddict-item]
    return out
