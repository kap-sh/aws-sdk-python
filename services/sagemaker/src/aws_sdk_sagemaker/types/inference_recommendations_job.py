"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendationsJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.model_package_arn
    import aws_sdk_sagemaker.types.recommendation_job_arn
    import aws_sdk_sagemaker.types.recommendation_job_description
    import aws_sdk_sagemaker.types.recommendation_job_name
    import aws_sdk_sagemaker.types.recommendation_job_status
    import aws_sdk_sagemaker.types.recommendation_job_type
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.s3_uri
    import aws_sdk_sagemaker.types.timestamp


class InferenceRecommendationsJob(TypedDict, closed=True):
    job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of the job.</p>"""
    job_description: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_description.RecommendationJobDescription"
    ]
    """<p>The job description.</p>"""
    job_type: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_type.RecommendationJobType"
    ]
    """<p>The recommendation job type.</p>"""
    job_arn: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_arn.RecommendationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recommendation job.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_status.RecommendationJobStatus"
    ]
    """<p>The status of the job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that shows when the job was created.</p>"""
    completion_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the job completed.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp that shows when the job was last modified.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the job fails, provides information why the job failed.</p>"""
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the created model.</p>"""
    sample_payload_url: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).</p>"""
    model_package_version_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a versioned model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendationsJob) -> dict:
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
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "sample_payload_url" in value:
        out["SamplePayloadUrl"] = value["sample_payload_url"]
    if "model_package_version_arn" in value:
        out["ModelPackageVersionArn"] = value["model_package_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceRecommendationsJob:
    out: InferenceRecommendationsJob = {}  # type: ignore[typeddict-item]
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
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "SamplePayloadUrl" in data:
        out["sample_payload_url"] = data["SamplePayloadUrl"]
    if "ModelPackageVersionArn" in data:
        out["model_package_version_arn"] = data["ModelPackageVersionArn"]
    return out
