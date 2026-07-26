"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupSelectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.backup_selection
    import capo_backup.types.string


class CreateBackupSelectionInput(TypedDict, closed=True):
    backup_plan_id: "capo_backup.types.string.string"
    """<p>The ID of the backup plan.</p>"""
    backup_selection: "capo_backup.types.backup_selection.BackupSelection"
    """<p>The body of a request to assign a set of resources to a backup plan.</p>"""
    creator_request_id: NotRequired["capo_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupSelectionInput) -> dict:
    out: dict = {}
    import capo_backup.types.backup_selection

    out["BackupSelection"] = capo_backup.types.backup_selection.serialize_json(
        value["backup_selection"]
    )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> CreateBackupSelectionInput:
    out: CreateBackupSelectionInput = {}  # type: ignore[typeddict-item]
    if "BackupSelection" in data:
        import capo_backup.types.backup_selection

        out["backup_selection"] = capo_backup.types.backup_selection.deserialize_json(
            data["BackupSelection"]
        )
    else:
        raise DeserializationError(
            "CreateBackupSelectionInput.backup_selection required"
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out
