"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_experiment_summary

InferenceExperimentList: TypeAlias = list[
    "capo_sagemaker.types.inference_experiment_summary.InferenceExperimentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExperimentList) -> list:
    import capo_sagemaker.types.inference_experiment_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_experiment_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceExperimentList:
    import capo_sagemaker.types.inference_experiment_summary

    out: InferenceExperimentList = []
    for item in data:
        out.append(
            capo_sagemaker.types.inference_experiment_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
