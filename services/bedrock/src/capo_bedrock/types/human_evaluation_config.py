"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanEvaluationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_dataset_metric_configs
    import capo_bedrock.types.human_evaluation_custom_metrics
    import capo_bedrock.types.human_workflow_config


class HumanEvaluationConfig(TypedDict, closed=True):
    human_workflow_config: NotRequired[
        "capo_bedrock.types.human_workflow_config.HumanWorkflowConfig"
    ]
    """<p>The parameters of the human workflow.</p>"""
    custom_metrics: NotRequired[
        "capo_bedrock.types.human_evaluation_custom_metrics.HumanEvaluationCustomMetrics"
    ]
    """<p>A <code>HumanEvaluationCustomMetric</code> object. It contains the names the metrics, how the metrics are to be evaluated, an optional description.</p>"""
    dataset_metric_configs: "capo_bedrock.types.evaluation_dataset_metric_configs.EvaluationDatasetMetricConfigs"
    """<p>Use to specify the metrics, task, and prompt dataset to be used in your model evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanEvaluationConfig) -> dict:
    out: dict = {}
    if "human_workflow_config" in value:
        import capo_bedrock.types.human_workflow_config

        out["humanWorkflowConfig"] = (
            capo_bedrock.types.human_workflow_config.serialize_json(
                value["human_workflow_config"]
            )
        )
    if "custom_metrics" in value:
        import capo_bedrock.types.human_evaluation_custom_metrics

        out["customMetrics"] = (
            capo_bedrock.types.human_evaluation_custom_metrics.serialize_json(
                value["custom_metrics"]
            )
        )
    import capo_bedrock.types.evaluation_dataset_metric_configs

    out["datasetMetricConfigs"] = (
        capo_bedrock.types.evaluation_dataset_metric_configs.serialize_json(
            value["dataset_metric_configs"]
        )
    )
    return out


def deserialize_json(data: dict) -> HumanEvaluationConfig:
    out: HumanEvaluationConfig = {}  # type: ignore[typeddict-item]
    if "humanWorkflowConfig" in data:
        import capo_bedrock.types.human_workflow_config

        out["human_workflow_config"] = (
            capo_bedrock.types.human_workflow_config.deserialize_json(
                data["humanWorkflowConfig"]
            )
        )
    if "customMetrics" in data:
        import capo_bedrock.types.human_evaluation_custom_metrics

        out["custom_metrics"] = (
            capo_bedrock.types.human_evaluation_custom_metrics.deserialize_json(
                data["customMetrics"]
            )
        )
    if "datasetMetricConfigs" in data:
        import capo_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            capo_bedrock.types.evaluation_dataset_metric_configs.deserialize_json(
                data["datasetMetricConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "HumanEvaluationConfig.dataset_metric_configs required"
        )
    return out
