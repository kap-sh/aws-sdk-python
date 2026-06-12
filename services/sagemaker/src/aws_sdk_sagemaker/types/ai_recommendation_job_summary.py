"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_entity_name
    import aws_sdk_sagemaker.types.ai_recommendation_job_arn
    import aws_sdk_sagemaker.types.ai_recommendation_job_status
    import aws_sdk_sagemaker.types.timestamp


class AIRecommendationJobSummary(TypedDict):
    ai_recommendation_job_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the recommendation job.</p>"""
    ai_recommendation_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_job_arn.AIRecommendationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recommendation job.</p>"""
    ai_recommendation_job_status: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_job_status.AIRecommendationJobStatus"
    ]
    """<p>The status of the recommendation job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the recommendation job was created.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the recommendation job completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationJobSummary) -> dict:
    out: dict = {}
    if "ai_recommendation_job_name" in value:
        out["AIRecommendationJobName"] = value["ai_recommendation_job_name"]
    if "ai_recommendation_job_arn" in value:
        out["AIRecommendationJobArn"] = value["ai_recommendation_job_arn"]
    if "ai_recommendation_job_status" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_job_status

        out["AIRecommendationJobStatus"] = (
            aws_sdk_sagemaker.types.ai_recommendation_job_status.serialize_aws_json_1_1(
                value["ai_recommendation_job_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationJobSummary:
    out: AIRecommendationJobSummary = {}  # type: ignore[typeddict-item]
    if "AIRecommendationJobName" in data:
        out["ai_recommendation_job_name"] = data["AIRecommendationJobName"]
    if "AIRecommendationJobArn" in data:
        out["ai_recommendation_job_arn"] = data["AIRecommendationJobArn"]
    if "AIRecommendationJobStatus" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_job_status

        out["ai_recommendation_job_status"] = (
            aws_sdk_sagemaker.types.ai_recommendation_job_status.deserialize_aws_json_1_1(
                data["AIRecommendationJobStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
