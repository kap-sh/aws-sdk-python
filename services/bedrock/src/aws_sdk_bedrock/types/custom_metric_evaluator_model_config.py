"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomMetricEvaluatorModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_models


class CustomMetricEvaluatorModelConfig(TypedDict, closed=True):
    bedrock_evaluator_models: "aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_models.CustomMetricBedrockEvaluatorModels"
    """<p>Defines the model you want to evaluate custom metrics in an Amazon Bedrock evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetricEvaluatorModelConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_models

    out["bedrockEvaluatorModels"] = (
        aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_models.serialize_json(
            value["bedrock_evaluator_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomMetricEvaluatorModelConfig:
    out: CustomMetricEvaluatorModelConfig = {}  # type: ignore[typeddict-item]
    if "bedrockEvaluatorModels" in data:
        import aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_models

        out["bedrock_evaluator_models"] = (
            aws_sdk_bedrock.types.custom_metric_bedrock_evaluator_models.deserialize_json(
                data["bedrockEvaluatorModels"]
            )
        )
    else:
        raise DeserializationError(
            "CustomMetricEvaluatorModelConfig.bedrock_evaluator_models required"
        )
    return out
