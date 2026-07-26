"""Generated from Smithy shape ``com.amazonaws.backup#StartRestoreJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.restore_job_id


class StartRestoreJobOutput(TypedDict, closed=True):
    restore_job_id: NotRequired["capo_backup.types.restore_job_id.RestoreJobId"]
    """<p>Uniquely identifies the job that restores a recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRestoreJobOutput) -> dict:
    out: dict = {}
    if "restore_job_id" in value:
        out["RestoreJobId"] = value["restore_job_id"]
    return out


def deserialize_json(data: dict) -> StartRestoreJobOutput:
    out: StartRestoreJobOutput = {}  # type: ignore[typeddict-item]
    if "RestoreJobId" in data:
        out["restore_job_id"] = data["RestoreJobId"]
    return out
