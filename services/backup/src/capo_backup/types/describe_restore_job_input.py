"""Generated from Smithy shape ``com.amazonaws.backup#DescribeRestoreJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.restore_job_id


class DescribeRestoreJobInput(TypedDict, closed=True):
    restore_job_id: "capo_backup.types.restore_job_id.RestoreJobId"
    """<p>Uniquely identifies the job that restores a recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRestoreJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRestoreJobInput:
    out: DescribeRestoreJobInput = {}  # type: ignore[typeddict-item]
    return out
