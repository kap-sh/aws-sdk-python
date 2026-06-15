"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_by
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_job_status
    import aws_sdk_sagemaker.types.training_plan_arn
    import aws_sdk_sagemaker.types.warm_pool_resource_status


class ListTrainingJobsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListTrainingJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of training jobs, use the token in the next request. </p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of training jobs to return in the response.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs created after the specified time (timestamp).</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs created before the specified time (timestamp).</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs modified after the specified time (timestamp).</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>A filter that returns only training jobs modified before the specified time (timestamp).</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the training job name. This filter returns only training jobs whose name contains the specified string.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>A filter that retrieves only training jobs with a specific status.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.sort_by.SortBy"]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""
    warm_pool_status_equals: NotRequired[
        "aws_sdk_sagemaker.types.warm_pool_resource_status.WarmPoolResourceStatus"
    ]
    """<p>A filter that retrieves only training jobs with a specific warm pool status.</p>"""
    training_plan_arn_equals: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    r"""<p>The Amazon Resource Name (ARN); of the training plan to filter training jobs by. For more information about reserving GPU capacity for your SageMaker training jobs using Amazon SageMaker Training Plan, see <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html\">CreateTrainingPlan</a> </code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
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
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.training_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_by

        out["SortBy"] = aws_sdk_sagemaker.types.sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "warm_pool_status_equals" in value:
        import aws_sdk_sagemaker.types.warm_pool_resource_status

        out["WarmPoolStatusEquals"] = (
            aws_sdk_sagemaker.types.warm_pool_resource_status.serialize_aws_json_1_1(
                value["warm_pool_status_equals"]
            )
        )
    if "training_plan_arn_equals" in value:
        out["TrainingPlanArnEquals"] = value["training_plan_arn_equals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingJobsRequest:
    out: ListTrainingJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
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
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.training_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_by

        out["sort_by"] = aws_sdk_sagemaker.types.sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "WarmPoolStatusEquals" in data:
        import aws_sdk_sagemaker.types.warm_pool_resource_status

        out["warm_pool_status_equals"] = (
            aws_sdk_sagemaker.types.warm_pool_resource_status.deserialize_aws_json_1_1(
                data["WarmPoolStatusEquals"]
            )
        )
    if "TrainingPlanArnEquals" in data:
        out["training_plan_arn_equals"] = data["TrainingPlanArnEquals"]
    return out
