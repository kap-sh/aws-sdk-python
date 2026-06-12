"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExpectedPerformanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_performance_metric

ExpectedPerformanceList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_recommendation_performance_metric.AIRecommendationPerformanceMetric"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpectedPerformanceList) -> list:
    import aws_sdk_sagemaker.types.ai_recommendation_performance_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_performance_metric.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExpectedPerformanceList:
    import aws_sdk_sagemaker.types.ai_recommendation_performance_metric

    out: ExpectedPerformanceList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_performance_metric.deserialize_aws_json_1_1(
                item
            )
        )
    return out
