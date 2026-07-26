"""Generated from Smithy shape ``com.amazonaws.batch#ListServiceJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.list_jobs_filter_list
    import capo_batch.types.service_job_status
    import capo_batch.types.string


class ListServiceJobsRequest(TypedDict, closed=True):
    job_queue: NotRequired["capo_batch.types.string.String"]
    """<p>The name or ARN of the job queue with which to list service jobs.</p>"""
    job_status: NotRequired["capo_batch.types.service_job_status.ServiceJobStatus"]
    """<p>The job status used to filter service jobs in the specified queue. If the <code>filters</code> parameter is specified, the <code>jobStatus</code> parameter is ignored and jobs with any status are returned. The exceptions are the <code>SHARE_IDENTIFIER</code> filter and <code>QUOTA_SHARE_NAME</code> filter, which can be used with <code>jobStatus</code>. If you don't specify a status, only <code>RUNNING</code> jobs are returned.</p> <note> <p>The <code>SHARE_IDENTIFIER</code> filter or <code>QUOTA_SHARE_NAME</code> filter can be used with the <code>jobStatus</code> field to filter results.</p> </note>"""
    max_results: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>ListServiceJobs</code> in paginated output. When this parameter is used, <code>ListServiceJobs</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceJobs</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceJobs</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListServiceJobs</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    filters: NotRequired["capo_batch.types.list_jobs_filter_list.ListJobsFilterList"]
    """<p>The filter to apply to the query. Only one filter can be used at a time. When the filter is used, <code>jobStatus</code> is ignored with the exception that <code>SHARE_IDENTIFIER</code> or <code>QUOTA_SHARE_NAME</code> and <code>jobStatus</code> can be used together. The results are sorted by the <code>createdAt</code> field, with the most recent jobs being first.</p> <note> <p>The <code>SHARE_IDENTIFIER</code> or <code>QUOTA_SHARE_NAME</code> filter and the <code>jobStatus</code> field can be used together to filter results.</p> </note> <dl> <dt>JOB_NAME</dt> <dd> <p>The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (*), the filter matches any job name that begins with the string before the '*'. This corresponds to the <code>jobName</code> value. For example, <code>test1</code> matches both <code>Test1</code> and <code>test1</code>, and <code>test1*</code> matches both <code>test1</code> and <code>Test10</code>. When the <code>JOB_NAME</code> filter is used, the results are grouped by the job name and version.</p> </dd> <dt>BEFORE_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's before the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>AFTER_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's after the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>SHARE_IDENTIFIER</dt> <dd> <p>The value for the filter is the fairshare scheduling share identifier.</p> </dd> <dt>QUOTA_SHARE_NAME</dt> <dd> <p>The value for the filter is the quota management share name.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceJobsRequest) -> dict:
    out: dict = {}
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "job_status" in value:
        import capo_batch.types.service_job_status

        out["jobStatus"] = capo_batch.types.service_job_status.serialize_json(
            value["job_status"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_batch.types.list_jobs_filter_list

        out["filters"] = capo_batch.types.list_jobs_filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListServiceJobsRequest:
    out: ListServiceJobsRequest = {}  # type: ignore[typeddict-item]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "jobStatus" in data:
        import capo_batch.types.service_job_status

        out["job_status"] = capo_batch.types.service_job_status.deserialize_json(
            data["jobStatus"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filters" in data:
        import capo_batch.types.list_jobs_filter_list

        out["filters"] = capo_batch.types.list_jobs_filter_list.deserialize_json(
            data["filters"]
        )
    return out
