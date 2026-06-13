"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_evaluation_custom_metric_config
    import aws_sdk_bedrock.types.evaluation_dataset_metric_configs
    import aws_sdk_bedrock.types.evaluator_model_config


class AutomatedEvaluationConfig(TypedDict):
    dataset_metric_configs: "aws_sdk_bedrock.types.evaluation_dataset_metric_configs.EvaluationDatasetMetricConfigs"
    """<p>Configuration details of the prompt datasets and metrics you want to use for your evaluation job.</p>"""
    evaluator_model_config: NotRequired[
        "aws_sdk_bedrock.types.evaluator_model_config.EvaluatorModelConfig"
    ]
    """<p>Contains the evaluator model configuration details. <code>EvaluatorModelConfig</code> is required for evaluation jobs that use a knowledge base or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.</p>"""
    custom_metric_config: NotRequired[
        "aws_sdk_bedrock.types.automated_evaluation_custom_metric_config.AutomatedEvaluationCustomMetricConfig"
    ]
    """<p>Defines the configuration of custom metrics to be used in an evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.evaluation_dataset_metric_configs

    out["datasetMetricConfigs"] = (
        aws_sdk_bedrock.types.evaluation_dataset_metric_configs.serialize_json(
            value["dataset_metric_configs"]
        )
    )
    if "evaluator_model_config" in value:
        import aws_sdk_bedrock.types.evaluator_model_config

        out["evaluatorModelConfig"] = (
            aws_sdk_bedrock.types.evaluator_model_config.serialize_json(
                value["evaluator_model_config"]
            )
        )
    if "custom_metric_config" in value:
        import aws_sdk_bedrock.types.automated_evaluation_custom_metric_config

        out["customMetricConfig"] = (
            aws_sdk_bedrock.types.automated_evaluation_custom_metric_config.serialize_json(
                value["custom_metric_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedEvaluationConfig:
    out: AutomatedEvaluationConfig = {}  # type: ignore[typeddict-item]
    if "datasetMetricConfigs" in data:
        import aws_sdk_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            aws_sdk_bedrock.types.evaluation_dataset_metric_configs.deserialize_json(
                data["datasetMetricConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedEvaluationConfig.dataset_metric_configs required"
        )
    if "evaluatorModelConfig" in data:
        import aws_sdk_bedrock.types.evaluator_model_config

        out["evaluator_model_config"] = (
            aws_sdk_bedrock.types.evaluator_model_config.deserialize_json(
                data["evaluatorModelConfig"]
            )
        )
    if "customMetricConfig" in data:
        import aws_sdk_bedrock.types.automated_evaluation_custom_metric_config

        out["custom_metric_config"] = (
            aws_sdk_bedrock.types.automated_evaluation_custom_metric_config.deserialize_json(
                data["customMetricConfig"]
            )
        )
    return out
