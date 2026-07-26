"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLabelingJobsForWorkteamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.job_reference_code_contains
    import capo_sagemaker.types.list_labeling_jobs_for_workteam_sort_by_options
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.workteam_arn


class ListLabelingJobsForWorkteamRequest(TypedDict, closed=True):
    workteam_arn: NotRequired["capo_sagemaker.types.workteam_arn.WorkteamArn"]
    """<p>The Amazon Resource Name (ARN) of the work team for which you want to see labeling jobs for.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of labeling jobs to return in each page of the response.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListLabelingJobsForWorkteam</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of labeling jobs, use the token in the next request.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only labeling jobs created after the specified time (timestamp).</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only labeling jobs created before the specified time (timestamp).</p>"""
    job_reference_code_contains: NotRequired[
        "capo_sagemaker.types.job_reference_code_contains.JobReferenceCodeContains"
    ]
    """<p>A filter the limits jobs to only the ones whose job reference code contains the specified string.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.list_labeling_jobs_for_workteam_sort_by_options.ListLabelingJobsForWorkteamSortByOptions"
    ]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLabelingJobsForWorkteamRequest) -> dict:
    out: dict = {}
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "job_reference_code_contains" in value:
        out["JobReferenceCodeContains"] = value["job_reference_code_contains"]
    if "sort_by" in value:
        import capo_sagemaker.types.list_labeling_jobs_for_workteam_sort_by_options

        out["SortBy"] = (
            capo_sagemaker.types.list_labeling_jobs_for_workteam_sort_by_options.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLabelingJobsForWorkteamRequest:
    out: ListLabelingJobsForWorkteamRequest = {}  # type: ignore[typeddict-item]
    if "WorkteamArn" in data:
        out["workteam_arn"] = data["WorkteamArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "JobReferenceCodeContains" in data:
        out["job_reference_code_contains"] = data["JobReferenceCodeContains"]
    if "SortBy" in data:
        import capo_sagemaker.types.list_labeling_jobs_for_workteam_sort_by_options

        out["sort_by"] = (
            capo_sagemaker.types.list_labeling_jobs_for_workteam_sort_by_options.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
