"""Generated from Smithy shape ``com.amazonaws.backup#StartRestoreJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_job_id


class StartRestoreJobOutput(TypedDict):
    restore_job_id: NotRequired["aws_sdk_backup.types.restore_job_id.RestoreJobId"]
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
