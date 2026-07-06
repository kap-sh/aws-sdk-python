"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHyperParameterTuningJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_sort_by_options
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListHyperParameterTuningJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListHyperParameterTuningJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of tuning jobs, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of tuning jobs to return. The default value is 10.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_sort_by_options.HyperParameterTuningJobSortByOptions"
    ]
    """<p>The field to sort results by. The default is <code>Name</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the tuning job name. This filter returns only tuning jobs whose name contains the specified string.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only tuning jobs that were created after the specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only tuning jobs that were created before the specified time.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only tuning jobs that were modified after the specified time.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>A filter that returns only tuning jobs that were modified before the specified time.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status.HyperParameterTuningJobStatus"
    ]
    """<p>A filter that returns only tuning jobs with the specified status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHyperParameterTuningJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_sort_by_options

        out["SortBy"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_sort_by_options.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHyperParameterTuningJobsRequest:
    out: ListHyperParameterTuningJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_sort_by_options

        out["sort_by"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_sort_by_options.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    return out
