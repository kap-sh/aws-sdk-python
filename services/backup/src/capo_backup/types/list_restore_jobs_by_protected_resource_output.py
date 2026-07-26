"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreJobsByProtectedResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.restore_jobs_list
    import capo_backup.types.string


class ListRestoreJobsByProtectedResourceOutput(TypedDict, closed=True):
    restore_jobs: NotRequired["capo_backup.types.restore_jobs_list.RestoreJobsList"]
    """<p>An array of objects that contain detailed information about jobs to restore saved resources.></p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows youto return more items in your list starting at the location pointed to by the next token</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreJobsByProtectedResourceOutput) -> dict:
    out: dict = {}
    if "restore_jobs" in value:
        import capo_backup.types.restore_jobs_list

        out["RestoreJobs"] = capo_backup.types.restore_jobs_list.serialize_json(
            value["restore_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRestoreJobsByProtectedResourceOutput:
    out: ListRestoreJobsByProtectedResourceOutput = {}  # type: ignore[typeddict-item]
    if "RestoreJobs" in data:
        import capo_backup.types.restore_jobs_list

        out["restore_jobs"] = capo_backup.types.restore_jobs_list.deserialize_json(
            data["RestoreJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
