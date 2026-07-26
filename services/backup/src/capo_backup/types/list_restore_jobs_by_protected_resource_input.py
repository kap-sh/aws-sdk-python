"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreJobsByProtectedResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.max_results
    import capo_backup.types.restore_job_status
    import capo_backup.types.string
    import capo_backup.types.timestamp


class ListRestoreJobsByProtectedResourceInput(TypedDict, closed=True):
    resource_arn: "capo_backup.types.arn.ARN"
    """<p>Returns only restore jobs that match the specified resource Amazon Resource Name (ARN).</p>"""
    by_status: NotRequired["capo_backup.types.restore_job_status.RestoreJobStatus"]
    """<p>Returns only restore jobs associated with the specified job status.</p>"""
    by_recovery_point_creation_date_after: NotRequired[
        "capo_backup.types.timestamp.timestamp"
    ]
    """<p>Returns only restore jobs of recovery points that were created after the specified date.</p>"""
    by_recovery_point_creation_date_before: NotRequired[
        "capo_backup.types.timestamp.timestamp"
    ]
    """<p>Returns only restore jobs of recovery points that were created before the specified date.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request ismade to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreJobsByProtectedResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRestoreJobsByProtectedResourceInput:
    out: ListRestoreJobsByProtectedResourceInput = {}  # type: ignore[typeddict-item]
    return out
