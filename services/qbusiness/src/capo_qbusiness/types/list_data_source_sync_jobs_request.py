"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataSourceSyncJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.data_source_sync_job_status
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.timestamp


class ListDataSourceSyncJobsRequest(TypedDict, closed=True):
    data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId"
    """<p> The identifier of the data source connector.</p>"""
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application connected to the data source.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index used with the Amazon Q Business data source connector.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incpmplete because there is more data to retriever, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of responses.</p>"""
    max_results: NotRequired[
        "capo_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs.MaxResultsIntegerForListDataSourcesSyncJobs"
    ]
    """<p>The maximum number of synchronization jobs to return in the response.</p>"""
    start_time: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p> The start time of the data source connector sync. </p>"""
    end_time: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p> The end time of the data source connector sync.</p>"""
    status_filter: NotRequired[
        "capo_qbusiness.types.data_source_sync_job_status.DataSourceSyncJobStatus"
    ]
    """<p>Only returns synchronization jobs with the <code>Status</code> field equal to the specified status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceSyncJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSourceSyncJobsRequest:
    out: ListDataSourceSyncJobsRequest = {}  # type: ignore[typeddict-item]
    return out
