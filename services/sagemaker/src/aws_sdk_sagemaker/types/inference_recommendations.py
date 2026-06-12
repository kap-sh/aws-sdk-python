"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_recommendation

InferenceRecommendations: TypeAlias = list[
    "aws_sdk_sagemaker.types.inference_recommendation.InferenceRecommendation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendations) -> list:
    import aws_sdk_sagemaker.types.inference_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.inference_recommendation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceRecommendations:
    import aws_sdk_sagemaker.types.inference_recommendation

    out: InferenceRecommendations = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.inference_recommendation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
