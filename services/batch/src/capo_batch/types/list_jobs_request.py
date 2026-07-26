"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.job_status
    import capo_batch.types.list_jobs_filter_list
    import capo_batch.types.string


class ListJobsRequest(TypedDict, closed=True):
    job_queue: NotRequired["capo_batch.types.string.String"]
    """<p>The name or full Amazon Resource Name (ARN) of the job queue used to list jobs.</p>"""
    array_job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.</p>"""
    multi_node_job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.</p>"""
    job_status: NotRequired["capo_batch.types.job_status.JobStatus"]
    """<p>The job status used to filter jobs in the specified queue. If the <code>filters</code> parameter is specified, the <code>jobStatus</code> parameter is ignored and jobs with any status are returned. The exception is the <code>SHARE_IDENTIFIER</code> filter and <code>jobStatus</code> can be used together. If you don't specify a status, only <code>RUNNING</code> jobs are returned.</p> <note> <p>Array job parents are updated to <code>PENDING</code> when any child job is updated to <code>RUNNABLE</code> and remain in <code>PENDING</code> status while child jobs are running. To view these jobs, filter by <code>PENDING</code> status until all child jobs reach a terminal state.</p> </note>"""
    max_results: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>ListJobs</code> in a paginated output. When this parameter is used, <code>ListJobs</code> returns up to <code>maxResults</code> results in a single page and a <code>nextToken</code> response element, if applicable. The remaining results of the initial request can be seen by sending another <code>ListJobs</code> request with the returned <code>nextToken</code> value.</p> <p>The following outlines key parameters and limitations:</p> <ul> <li> <p>The minimum value is 1. </p> </li> <li> <p>When <code>--job-status</code> is used, Batch returns up to 1000 values. </p> </li> <li> <p>When <code>--filters</code> is used, Batch returns up to 100 values.</p> </li> <li> <p>If neither parameter is used, then <code>ListJobs</code> returns up to 1000 results (jobs that are in the <code>RUNNING</code> status) and a <code>nextToken</code> value, if applicable.</p> </li> </ul>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListJobs</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    filters: NotRequired["capo_batch.types.list_jobs_filter_list.ListJobsFilterList"]
    """<p>The filter to apply to the query. Only one filter can be used at a time. When the filter is used, <code>jobStatus</code> is ignored with the exception that <code>SHARE_IDENTIFIER</code> and <code>jobStatus</code> can be used together. The filter doesn't apply to child jobs in an array or multi-node parallel (MNP) jobs. The results are sorted by the <code>createdAt</code> field, with the most recent jobs being first.</p> <note> <p>The <code>SHARE_IDENTIFIER</code> filter and the <code>jobStatus</code> field can be used together to filter results.</p> </note> <dl> <dt>JOB_NAME</dt> <dd> <p>The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (*), the filter matches any job name that begins with the string before the '*'. This corresponds to the <code>jobName</code> value. For example, <code>test1</code> matches both <code>Test1</code> and <code>test1</code>, and <code>test1*</code> matches both <code>test1</code> and <code>Test10</code>. When the <code>JOB_NAME</code> filter is used, the results are grouped by the job name and version.</p> </dd> <dt>JOB_DEFINITION</dt> <dd> <p>The value for the filter is the name or Amazon Resource Name (ARN) of the job definition. This corresponds to the <code>jobDefinition</code> value. The value is case sensitive. When the value for the filter is the job definition name, the results include all the jobs that used any revision of that job definition name. If the value ends with an asterisk (*), the filter matches any job definition name that begins with the string before the '*'. For example, <code>jd1</code> matches only <code>jd1</code>, and <code>jd1*</code> matches both <code>jd1</code> and <code>jd1A</code>. The version of the job definition that's used doesn't affect the sort order. When the <code>JOB_DEFINITION</code> filter is used and the ARN is used (which is in the form <code>arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}</code>), the results include jobs that used the specified revision of the job definition. Asterisk (*) isn't supported when the ARN is used.</p> </dd> <dt>BEFORE_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's before the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>AFTER_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's after the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>SHARE_IDENTIFIER</dt> <dd> <p>The value for the filter is the fairshare scheduling share identifier.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsRequest) -> dict:
    out: dict = {}
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "array_job_id" in value:
        out["arrayJobId"] = value["array_job_id"]
    if "multi_node_job_id" in value:
        out["multiNodeJobId"] = value["multi_node_job_id"]
    if "job_status" in value:
        import capo_batch.types.job_status

        out["jobStatus"] = capo_batch.types.job_status.serialize_json(
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


def deserialize_json(data: dict) -> ListJobsRequest:
    out: ListJobsRequest = {}  # type: ignore[typeddict-item]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "arrayJobId" in data:
        out["array_job_id"] = data["arrayJobId"]
    if "multiNodeJobId" in data:
        out["multi_node_job_id"] = data["multiNodeJobId"]
    if "jobStatus" in data:
        import capo_batch.types.job_status

        out["job_status"] = capo_batch.types.job_status.deserialize_json(
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
