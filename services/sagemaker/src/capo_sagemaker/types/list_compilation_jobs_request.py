"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCompilationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compilation_job_status
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.list_compilation_jobs_sort_by
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order


class ListCompilationJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListCompilationJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of model compilation jobs, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of model compilation jobs to return in the response.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A filter that returns the model compilation jobs that were created after a specified time. </p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A filter that returns the model compilation jobs that were created before a specified time.</p>"""
    last_modified_time_after: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns the model compilation jobs that were modified after a specified time.</p>"""
    last_modified_time_before: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns the model compilation jobs that were modified before a specified time.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>A filter that returns the model compilation jobs whose name contains a specified string.</p>"""
    status_equals: NotRequired[
        "capo_sagemaker.types.compilation_job_status.CompilationJobStatus"
    ]
    """<p>A filter that retrieves model compilation jobs with a specific <code>CompilationJobStatus</code> status.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.list_compilation_jobs_sort_by.ListCompilationJobsSortBy"
    ]
    """<p>The field by which to sort results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCompilationJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "creation_time_after" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTimeAfter"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTimeBefore"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import capo_sagemaker.types.compilation_job_status

        out["StatusEquals"] = (
            capo_sagemaker.types.compilation_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import capo_sagemaker.types.list_compilation_jobs_sort_by

        out["SortBy"] = (
            capo_sagemaker.types.list_compilation_jobs_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCompilationJobsRequest:
    out: ListCompilationJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time_after"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time_before"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time_after"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time_before"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "StatusEquals" in data:
        import capo_sagemaker.types.compilation_job_status

        out["status_equals"] = (
            capo_sagemaker.types.compilation_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import capo_sagemaker.types.list_compilation_jobs_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.list_compilation_jobs_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
