"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_recommendation_job_summary

AIRecommendationJobSummaryList: TypeAlias = list[
    "capo_sagemaker.types.ai_recommendation_job_summary.AIRecommendationJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationJobSummaryList) -> list:
    import capo_sagemaker.types.ai_recommendation_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_recommendation_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationJobSummaryList:
    import capo_sagemaker.types.ai_recommendation_job_summary

    out: AIRecommendationJobSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_recommendation_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
