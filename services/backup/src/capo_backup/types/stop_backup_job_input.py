"""Generated from Smithy shape ``com.amazonaws.backup#StopBackupJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string


class StopBackupJobInput(TypedDict, closed=True):
    backup_job_id: "capo_backup.types.string.string"
    """<p>Uniquely identifies a request to Backup to back up a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBackupJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopBackupJobInput:
    out: StopBackupJobInput = {}  # type: ignore[typeddict-item]
    return out
