"""Generated from Smithy shape ``com.amazonaws.backup#ListCopyJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.copy_jobs_list
    import capo_backup.types.string


class ListCopyJobsOutput(TypedDict, closed=True):
    copy_jobs: NotRequired["capo_backup.types.copy_jobs_list.CopyJobsList"]
    """<p>An array of structures containing metadata about your copy jobs returned in JSON format. </p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return MaxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCopyJobsOutput) -> dict:
    out: dict = {}
    if "copy_jobs" in value:
        import capo_backup.types.copy_jobs_list

        out["CopyJobs"] = capo_backup.types.copy_jobs_list.serialize_json(
            value["copy_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCopyJobsOutput:
    out: ListCopyJobsOutput = {}  # type: ignore[typeddict-item]
    if "CopyJobs" in data:
        import capo_backup.types.copy_jobs_list

        out["copy_jobs"] = capo_backup.types.copy_jobs_list.deserialize_json(
            data["CopyJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
