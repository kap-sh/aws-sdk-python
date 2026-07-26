"""Generated from Smithy shape ``com.amazonaws.sagemaker#RealTimeInferenceRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.real_time_inference_recommendation

RealTimeInferenceRecommendations: TypeAlias = list[
    "capo_sagemaker.types.real_time_inference_recommendation.RealTimeInferenceRecommendation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RealTimeInferenceRecommendations) -> list:
    import capo_sagemaker.types.real_time_inference_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.real_time_inference_recommendation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RealTimeInferenceRecommendations:
    import capo_sagemaker.types.real_time_inference_recommendation

    out: RealTimeInferenceRecommendations = []
    for item in data:
        out.append(
            capo_sagemaker.types.real_time_inference_recommendation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
