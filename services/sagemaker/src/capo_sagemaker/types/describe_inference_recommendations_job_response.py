"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceRecommendationsJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.endpoint_performances
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.inference_recommendations
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.recommendation_job_arn
    import capo_sagemaker.types.recommendation_job_description
    import capo_sagemaker.types.recommendation_job_input_config
    import capo_sagemaker.types.recommendation_job_name
    import capo_sagemaker.types.recommendation_job_status
    import capo_sagemaker.types.recommendation_job_stopping_conditions
    import capo_sagemaker.types.recommendation_job_type
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp


class DescribeInferenceRecommendationsJobResponse(TypedDict, closed=True):
    job_name: NotRequired[
        "capo_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of the job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    job_description: NotRequired[
        "capo_sagemaker.types.recommendation_job_description.RecommendationJobDescription"
    ]
    """<p>The job description that you provided when you initiated the job.</p>"""
    job_type: NotRequired[
        "capo_sagemaker.types.recommendation_job_type.RecommendationJobType"
    ]
    """<p>The job type that you provided when you initiated the job.</p>"""
    job_arn: NotRequired[
        "capo_sagemaker.types.recommendation_job_arn.RecommendationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role you provided when you initiated the job.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.recommendation_job_status.RecommendationJobStatus"
    ]
    """<p>The status of the job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that shows when the job was created.</p>"""
    completion_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the job completed.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp that shows when the job was last modified.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the job fails, provides information why the job failed.</p>"""
    input_config: NotRequired[
        "capo_sagemaker.types.recommendation_job_input_config.RecommendationJobInputConfig"
    ]
    """<p>Returns information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations you provided when you initiated the job.</p>"""
    stopping_conditions: NotRequired[
        "capo_sagemaker.types.recommendation_job_stopping_conditions.RecommendationJobStoppingConditions"
    ]
    """<p>The stopping conditions that you provided when you initiated the job.</p>"""
    inference_recommendations: NotRequired[
        "capo_sagemaker.types.inference_recommendations.InferenceRecommendations"
    ]
    """<p>The recommendations made by Inference Recommender.</p>"""
    endpoint_performances: NotRequired[
        "capo_sagemaker.types.endpoint_performances.EndpointPerformances"
    ]
    """<p>The performance results from running an Inference Recommender job on an existing endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInferenceRecommendationsJobResponse) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_description" in value:
        out["JobDescription"] = value["job_description"]
    if "job_type" in value:
        import capo_sagemaker.types.recommendation_job_type

        out["JobType"] = (
            capo_sagemaker.types.recommendation_job_type.serialize_aws_json_1_1(
                value["job_type"]
            )
        )
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        import capo_sagemaker.types.recommendation_job_status

        out["Status"] = (
            capo_sagemaker.types.recommendation_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "completion_time" in value:
        import capo_sagemaker.types.timestamp

        out["CompletionTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["completion_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "input_config" in value:
        import capo_sagemaker.types.recommendation_job_input_config

        out["InputConfig"] = (
            capo_sagemaker.types.recommendation_job_input_config.serialize_aws_json_1_1(
                value["input_config"]
            )
        )
    if "stopping_conditions" in value:
        import capo_sagemaker.types.recommendation_job_stopping_conditions

        out["StoppingConditions"] = (
            capo_sagemaker.types.recommendation_job_stopping_conditions.serialize_aws_json_1_1(
                value["stopping_conditions"]
            )
        )
    if "inference_recommendations" in value:
        import capo_sagemaker.types.inference_recommendations

        out["InferenceRecommendations"] = (
            capo_sagemaker.types.inference_recommendations.serialize_aws_json_1_1(
                value["inference_recommendations"]
            )
        )
    if "endpoint_performances" in value:
        import capo_sagemaker.types.endpoint_performances

        out["EndpointPerformances"] = (
            capo_sagemaker.types.endpoint_performances.serialize_aws_json_1_1(
                value["endpoint_performances"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInferenceRecommendationsJobResponse:
    out: DescribeInferenceRecommendationsJobResponse = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobDescription" in data:
        out["job_description"] = data["JobDescription"]
    if "JobType" in data:
        import capo_sagemaker.types.recommendation_job_type

        out["job_type"] = (
            capo_sagemaker.types.recommendation_job_type.deserialize_aws_json_1_1(
                data["JobType"]
            )
        )
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Status" in data:
        import capo_sagemaker.types.recommendation_job_status

        out["status"] = (
            capo_sagemaker.types.recommendation_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import capo_sagemaker.types.timestamp

        out["completion_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "InputConfig" in data:
        import capo_sagemaker.types.recommendation_job_input_config

        out["input_config"] = (
            capo_sagemaker.types.recommendation_job_input_config.deserialize_aws_json_1_1(
                data["InputConfig"]
            )
        )
    if "StoppingConditions" in data:
        import capo_sagemaker.types.recommendation_job_stopping_conditions

        out["stopping_conditions"] = (
            capo_sagemaker.types.recommendation_job_stopping_conditions.deserialize_aws_json_1_1(
                data["StoppingConditions"]
            )
        )
    if "InferenceRecommendations" in data:
        import capo_sagemaker.types.inference_recommendations

        out["inference_recommendations"] = (
            capo_sagemaker.types.inference_recommendations.deserialize_aws_json_1_1(
                data["InferenceRecommendations"]
            )
        )
    if "EndpointPerformances" in data:
        import capo_sagemaker.types.endpoint_performances

        out["endpoint_performances"] = (
            capo_sagemaker.types.endpoint_performances.deserialize_aws_json_1_1(
                data["EndpointPerformances"]
            )
        )
    return out
