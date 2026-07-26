"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_jobs_list
    import capo_backup.types.string


class ListBackupJobsOutput(TypedDict, closed=True):
    backup_jobs: NotRequired["capo_backup.types.backup_jobs_list.BackupJobsList"]
    """<p>An array of structures containing metadata about your backup jobs returned in JSON format.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupJobsOutput) -> dict:
    out: dict = {}
    if "backup_jobs" in value:
        import capo_backup.types.backup_jobs_list

        out["BackupJobs"] = capo_backup.types.backup_jobs_list.serialize_json(
            value["backup_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBackupJobsOutput:
    out: ListBackupJobsOutput = {}  # type: ignore[typeddict-item]
    if "BackupJobs" in data:
        import capo_backup.types.backup_jobs_list

        out["backup_jobs"] = capo_backup.types.backup_jobs_list.deserialize_json(
            data["BackupJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
