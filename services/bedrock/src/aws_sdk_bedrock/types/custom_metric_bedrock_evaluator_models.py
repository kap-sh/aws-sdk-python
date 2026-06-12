"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomMetricBedrockEvaluatorModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_model

CustomMetricBedrockEvaluatorModels: TypeAlias = list[
    "aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_model.CustomMetricBedrockEvaluatorModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetricBedrockEvaluatorModels) -> list:
    import aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_model.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomMetricBedrockEvaluatorModels:
    import aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_model

    out: CustomMetricBedrockEvaluatorModels = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_model.deserialize_json(
                item
            )
        )
    return out
