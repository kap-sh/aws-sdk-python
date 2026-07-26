"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentStageStatusSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.deployment_stage_status_summary

DeploymentStageStatusSummaries: TypeAlias = list[
    "capo_sagemaker.types.deployment_stage_status_summary.DeploymentStageStatusSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStageStatusSummaries) -> list:
    import capo_sagemaker.types.deployment_stage_status_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.deployment_stage_status_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentStageStatusSummaries:
    import capo_sagemaker.types.deployment_stage_status_summary

    out: DeploymentStageStatusSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.deployment_stage_status_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
