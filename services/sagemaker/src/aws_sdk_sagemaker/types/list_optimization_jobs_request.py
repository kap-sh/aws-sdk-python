"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListOptimizationJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.list_optimization_jobs_sort_by
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.optimization_job_status
    import aws_sdk_sagemaker.types.sort_order


class ListOptimizationJobsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token that you use to get the next set of results following a truncated response. If the response to the previous request was truncated, that response provides the value for this token.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of optimization jobs to return in the response. The default is 50.</p>"""
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>Filters the results to only those optimization jobs that were created after the specified time.</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>Filters the results to only those optimization jobs that were created before the specified time.</p>"""
    last_modified_time_after: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Filters the results to only those optimization jobs that were updated after the specified time.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Filters the results to only those optimization jobs that were updated before the specified time.</p>"""
    optimization_contains: NotRequired[
        "aws_sdk_sagemaker.types.name_contains.NameContains"
    ]
    """<p>Filters the results to only those optimization jobs that apply the specified optimization techniques. You can specify either <code>Quantization</code> or <code>Compilation</code>.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>Filters the results to only those optimization jobs with a name that contains the specified string.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_status.OptimizationJobStatus"
    ]
    """<p>Filters the results to only those optimization jobs with the specified status.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.list_optimization_jobs_sort_by.ListOptimizationJobsSortBy"
    ]
    """<p>The field by which to sort the optimization jobs in the response. The default is <code>CreationTime</code> </p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOptimizationJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "optimization_contains" in value:
        out["OptimizationContains"] = value["optimization_contains"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.optimization_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.optimization_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.list_optimization_jobs_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.list_optimization_jobs_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOptimizationJobsRequest:
    out: ListOptimizationJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "OptimizationContains" in data:
        out["optimization_contains"] = data["OptimizationContains"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.optimization_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.optimization_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.list_optimization_jobs_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.list_optimization_jobs_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
