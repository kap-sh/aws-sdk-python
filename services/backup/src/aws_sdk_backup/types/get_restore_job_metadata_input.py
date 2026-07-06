"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreJobMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_job_id


class GetRestoreJobMetadataInput(TypedDict, closed=True):
    restore_job_id: "aws_sdk_backup.types.restore_job_id.RestoreJobId"
    """<p>This is a unique identifier of a restore job within Backup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreJobMetadataInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRestoreJobMetadataInput:
    out: GetRestoreJobMetadataInput = {}  # type: ignore[typeddict-item]
    return out
