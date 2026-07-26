"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExperimentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_summary

ExperimentSummaries: TypeAlias = list[
    "capo_sagemaker.types.experiment_summary.ExperimentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperimentSummaries) -> list:
    import capo_sagemaker.types.experiment_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.experiment_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExperimentSummaries:
    import capo_sagemaker.types.experiment_summary

    out: ExperimentSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.experiment_summary.deserialize_aws_json_1_1(item)
        )
    return out
