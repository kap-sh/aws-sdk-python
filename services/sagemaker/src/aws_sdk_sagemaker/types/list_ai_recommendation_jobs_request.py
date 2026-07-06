"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIRecommendationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_job_status
    import aws_sdk_sagemaker.types.list_ai_recommendation_jobs_sort_by
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListAIRecommendationJobsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of recommendation jobs to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListAIRecommendationJobs</code> didn't return the full set of jobs, the call returns a token for getting the next set.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the job name. This filter returns only jobs whose name contains the specified string.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_job_status.AIRecommendationJobStatus"
    ]
    """<p>A filter that returns only recommendation jobs with the specified status.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only jobs created after the specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only jobs created before the specified time.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.list_ai_recommendation_jobs_sort_by.ListAIRecommendationJobsSortBy"
    ]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Descending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIRecommendationJobsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.ai_recommendation_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
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
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.list_ai_recommendation_jobs_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.list_ai_recommendation_jobs_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAIRecommendationJobsRequest:
    out: ListAIRecommendationJobsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.ai_recommendation_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
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
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.list_ai_recommendation_jobs_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.list_ai_recommendation_jobs_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
