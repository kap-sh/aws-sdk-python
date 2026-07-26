"""Generated from Smithy shape ``com.amazonaws.backup#DescribeBackupJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string


class DescribeBackupJobInput(TypedDict, closed=True):
    backup_job_id: "capo_backup.types.string.string"
    """<p>Uniquely identifies a request to Backup to back up a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBackupJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBackupJobInput:
    out: DescribeBackupJobInput = {}  # type: ignore[typeddict-item]
    return out
