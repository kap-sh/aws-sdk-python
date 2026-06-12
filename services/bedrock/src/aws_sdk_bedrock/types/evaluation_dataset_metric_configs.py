"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationDatasetMetricConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_dataset_metric_config

EvaluationDatasetMetricConfigs: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_dataset_metric_config.EvaluationDatasetMetricConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDatasetMetricConfigs) -> list:
    import aws_sdk_bedrock.types.evaluation_dataset_metric_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.evaluation_dataset_metric_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationDatasetMetricConfigs:
    import aws_sdk_bedrock.types.evaluation_dataset_metric_config

    out: EvaluationDatasetMetricConfigs = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.evaluation_dataset_metric_config.deserialize_json(
                item
            )
        )
    return out
