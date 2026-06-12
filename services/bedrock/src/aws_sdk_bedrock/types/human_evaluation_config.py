"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanEvaluationConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_dataset_metric_configs
    import aws_sdk_bedrock.types.human_evaluation_custom_metrics
    import aws_sdk_bedrock.types.human_workflow_config


class HumanEvaluationConfig(TypedDict):
    human_workflow_config: NotRequired[
        "aws_sdk_bedrock.types.human_workflow_config.HumanWorkflowConfig"
    ]
    """<p>The parameters of the human workflow.</p>"""
    custom_metrics: NotRequired[
        "aws_sdk_bedrock.types.human_evaluation_custom_metrics.HumanEvaluationCustomMetrics"
    ]
    """<p>A <code>HumanEvaluationCustomMetric</code> object. It contains the names the metrics, how the metrics are to be evaluated, an optional description.</p>"""
    dataset_metric_configs: "aws_sdk_bedrock.types.evaluation_dataset_metric_configs.EvaluationDatasetMetricConfigs"
    """<p>Use to specify the metrics, task, and prompt dataset to be used in your model evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanEvaluationConfig) -> dict:
    out: dict = {}
    if "human_workflow_config" in value:
        import aws_sdk_bedrock.types.human_workflow_config

        out["humanWorkflowConfig"] = (
            aws_sdk_bedrock.types.human_workflow_config.serialize_json(
                value["human_workflow_config"]
            )
        )
    if "custom_metrics" in value:
        import aws_sdk_bedrock.types.human_evaluation_custom_metrics

        out["customMetrics"] = (
            aws_sdk_bedrock.types.human_evaluation_custom_metrics.serialize_json(
                value["custom_metrics"]
            )
        )
    import aws_sdk_bedrock.types.evaluation_dataset_metric_configs

    out["datasetMetricConfigs"] = (
        aws_sdk_bedrock.types.evaluation_dataset_metric_configs.serialize_json(
            value["dataset_metric_configs"]
        )
    )
    return out


def deserialize_json(data: dict) -> HumanEvaluationConfig:
    out: HumanEvaluationConfig = {}  # type: ignore[typeddict-item]
    if "humanWorkflowConfig" in data:
        import aws_sdk_bedrock.types.human_workflow_config

        out["human_workflow_config"] = (
            aws_sdk_bedrock.types.human_workflow_config.deserialize_json(
                data["humanWorkflowConfig"]
            )
        )
    if "customMetrics" in data:
        import aws_sdk_bedrock.types.human_evaluation_custom_metrics

        out["custom_metrics"] = (
            aws_sdk_bedrock.types.human_evaluation_custom_metrics.deserialize_json(
                data["customMetrics"]
            )
        )
    if "datasetMetricConfigs" in data:
        import aws_sdk_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            aws_sdk_bedrock.types.evaluation_dataset_metric_configs.deserialize_json(
                data["datasetMetricConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "HumanEvaluationConfig.dataset_metric_configs required"
        )
    return out
