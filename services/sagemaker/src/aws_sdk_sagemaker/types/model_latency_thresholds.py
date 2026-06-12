"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelLatencyThresholds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_latency_threshold

ModelLatencyThresholds: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_latency_threshold.ModelLatencyThreshold"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelLatencyThresholds) -> list:
    import aws_sdk_sagemaker.types.model_latency_threshold

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_latency_threshold.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelLatencyThresholds:
    import aws_sdk_sagemaker.types.model_latency_threshold

    out: ModelLatencyThresholds = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_latency_threshold.deserialize_aws_json_1_1(
                item
            )
        )
    return out
