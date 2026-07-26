"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataSourceSyncJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_sync_jobs
    import capo_qbusiness.types.next_token


class ListDataSourceSyncJobsResponse(TypedDict, closed=True):
    history: NotRequired[
        "capo_qbusiness.types.data_source_sync_jobs.DataSourceSyncJobs"
    ]
    """<p>A history of synchronization jobs for the data source connector.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token. You can use this token in any subsequent request to retrieve the next set of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceSyncJobsResponse) -> dict:
    out: dict = {}
    if "history" in value:
        import capo_qbusiness.types.data_source_sync_jobs

        out["history"] = capo_qbusiness.types.data_source_sync_jobs.serialize_json(
            value["history"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSourceSyncJobsResponse:
    out: ListDataSourceSyncJobsResponse = {}  # type: ignore[typeddict-item]
    if "history" in data:
        import capo_qbusiness.types.data_source_sync_jobs

        out["history"] = capo_qbusiness.types.data_source_sync_jobs.deserialize_json(
            data["history"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
