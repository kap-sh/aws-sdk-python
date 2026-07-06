"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.list_inference_recommendations_jobs_sort_by
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.model_package_arn
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.recommendation_job_status
    import aws_sdk_sagemaker.types.sort_order


class ListInferenceRecommendationsJobsRequest(TypedDict, closed=True):
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only jobs created after the specified time (timestamp).</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only jobs created before the specified time (timestamp).</p>"""
    last_modified_time_after: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns only jobs that were last modified after the specified time (timestamp).</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns only jobs that were last modified before the specified time (timestamp).</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the job name. This filter returns only recommendations whose name contains the specified string.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_status.RecommendationJobStatus"
    ]
    """<p>A filter that retrieves only inference recommendations jobs with a specific status.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.list_inference_recommendations_jobs_sort_by.ListInferenceRecommendationsJobsSortBy"
    ]
    """<p>The parameter by which to sort the results.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for the results.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListInferenceRecommendationsJobsRequest</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of recommendations, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of recommendations to return in the response.</p>"""
    model_name_equals: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>A filter that returns only jobs that were created for this model.</p>"""
    model_package_version_arn_equals: NotRequired[
        "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>A filter that returns only jobs that were created for this versioned model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobsRequest) -> dict:
    out: dict = {}
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
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.recommendation_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.recommendation_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.list_inference_recommendations_jobs_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.list_inference_recommendations_jobs_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "model_name_equals" in value:
        out["ModelNameEquals"] = value["model_name_equals"]
    if "model_package_version_arn_equals" in value:
        out["ModelPackageVersionArnEquals"] = value["model_package_version_arn_equals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceRecommendationsJobsRequest:
    out: ListInferenceRecommendationsJobsRequest = {}  # type: ignore[typeddict-item]
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
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.recommendation_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.recommendation_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.list_inference_recommendations_jobs_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.list_inference_recommendations_jobs_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ModelNameEquals" in data:
        out["model_name_equals"] = data["ModelNameEquals"]
    if "ModelPackageVersionArnEquals" in data:
        out["model_package_version_arn_equals"] = data["ModelPackageVersionArnEquals"]
    return out
