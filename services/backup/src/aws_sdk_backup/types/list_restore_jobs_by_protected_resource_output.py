"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreJobsByProtectedResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_jobs_list
    import aws_sdk_backup.types.string


class ListRestoreJobsByProtectedResourceOutput(TypedDict):
    restore_jobs: NotRequired["aws_sdk_backup.types.restore_jobs_list.RestoreJobsList"]
    """<p>An array of objects that contain detailed information about jobs to restore saved resources.></p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows youto return more items in your list starting at the location pointed to by the next token</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreJobsByProtectedResourceOutput) -> dict:
    out: dict = {}
    if "restore_jobs" in value:
        import aws_sdk_backup.types.restore_jobs_list

        out["RestoreJobs"] = aws_sdk_backup.types.restore_jobs_list.serialize_json(
            value["restore_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRestoreJobsByProtectedResourceOutput:
    out: ListRestoreJobsByProtectedResourceOutput = {}  # type: ignore[typeddict-item]
    if "RestoreJobs" in data:
        import aws_sdk_backup.types.restore_jobs_list

        out["restore_jobs"] = aws_sdk_backup.types.restore_jobs_list.deserialize_json(
            data["RestoreJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
