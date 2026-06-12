"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceRecommendationsJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.endpoint_performances
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.inference_recommendations
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.recommendation_job_arn
    import aws_sdk_sagemaker.types.recommendation_job_description
    import aws_sdk_sagemaker.types.recommendation_job_input_config
    import aws_sdk_sagemaker.types.recommendation_job_name
    import aws_sdk_sagemaker.types.recommendation_job_status
    import aws_sdk_sagemaker.types.recommendation_job_stopping_conditions
    import aws_sdk_sagemaker.types.recommendation_job_type
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeInferenceRecommendationsJobResponse(TypedDict):
    job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of the job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    job_description: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_description.RecommendationJobDescription"
    ]
    """<p>The job description that you provided when you initiated the job.</p>"""
    job_type: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_type.RecommendationJobType"
    ]
    """<p>The job type that you provided when you initiated the job.</p>"""
    job_arn: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_arn.RecommendationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role you provided when you initiated the job.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_status.RecommendationJobStatus"
    ]
    """<p>The status of the job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that shows when the job was created.</p>"""
    completion_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the job completed.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp that shows when the job was last modified.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the job fails, provides information why the job failed.</p>"""
    input_config: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_input_config.RecommendationJobInputConfig"
    ]
    """<p>Returns information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations you provided when you initiated the job.</p>"""
    stopping_conditions: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_stopping_conditions.RecommendationJobStoppingConditions"
    ]
    """<p>The stopping conditions that you provided when you initiated the job.</p>"""
    inference_recommendations: NotRequired[
        "aws_sdk_sagemaker.types.inference_recommendations.InferenceRecommendations"
    ]
    """<p>The recommendations made by Inference Recommender.</p>"""
    endpoint_performances: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_performances.EndpointPerformances"
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
        import aws_sdk_sagemaker.types.recommendation_job_type

        out["JobType"] = (
            aws_sdk_sagemaker.types.recommendation_job_type.serialize_aws_json_1_1(
                value["job_type"]
            )
        )
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        import aws_sdk_sagemaker.types.recommendation_job_status

        out["Status"] = (
            aws_sdk_sagemaker.types.recommendation_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "completion_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CompletionTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["completion_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "input_config" in value:
        import aws_sdk_sagemaker.types.recommendation_job_input_config

        out["InputConfig"] = (
            aws_sdk_sagemaker.types.recommendation_job_input_config.serialize_aws_json_1_1(
                value["input_config"]
            )
        )
    if "stopping_conditions" in value:
        import aws_sdk_sagemaker.types.recommendation_job_stopping_conditions

        out["StoppingConditions"] = (
            aws_sdk_sagemaker.types.recommendation_job_stopping_conditions.serialize_aws_json_1_1(
                value["stopping_conditions"]
            )
        )
    if "inference_recommendations" in value:
        import aws_sdk_sagemaker.types.inference_recommendations

        out["InferenceRecommendations"] = (
            aws_sdk_sagemaker.types.inference_recommendations.serialize_aws_json_1_1(
                value["inference_recommendations"]
            )
        )
    if "endpoint_performances" in value:
        import aws_sdk_sagemaker.types.endpoint_performances

        out["EndpointPerformances"] = (
            aws_sdk_sagemaker.types.endpoint_performances.serialize_aws_json_1_1(
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
        import aws_sdk_sagemaker.types.recommendation_job_type

        out["job_type"] = (
            aws_sdk_sagemaker.types.recommendation_job_type.deserialize_aws_json_1_1(
                data["JobType"]
            )
        )
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.recommendation_job_status

        out["status"] = (
            aws_sdk_sagemaker.types.recommendation_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["completion_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "InputConfig" in data:
        import aws_sdk_sagemaker.types.recommendation_job_input_config

        out["input_config"] = (
            aws_sdk_sagemaker.types.recommendation_job_input_config.deserialize_aws_json_1_1(
                data["InputConfig"]
            )
        )
    if "StoppingConditions" in data:
        import aws_sdk_sagemaker.types.recommendation_job_stopping_conditions

        out["stopping_conditions"] = (
            aws_sdk_sagemaker.types.recommendation_job_stopping_conditions.deserialize_aws_json_1_1(
                data["StoppingConditions"]
            )
        )
    if "InferenceRecommendations" in data:
        import aws_sdk_sagemaker.types.inference_recommendations

        out["inference_recommendations"] = (
            aws_sdk_sagemaker.types.inference_recommendations.deserialize_aws_json_1_1(
                data["InferenceRecommendations"]
            )
        )
    if "EndpointPerformances" in data:
        import aws_sdk_sagemaker.types.endpoint_performances

        out["endpoint_performances"] = (
            aws_sdk_sagemaker.types.endpoint_performances.deserialize_aws_json_1_1(
                data["EndpointPerformances"]
            )
        )
    return out
