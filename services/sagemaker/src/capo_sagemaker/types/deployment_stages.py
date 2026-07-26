"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentStages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.deployment_stage

DeploymentStages: TypeAlias = list[
    "capo_sagemaker.types.deployment_stage.DeploymentStage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStages) -> list:
    import capo_sagemaker.types.deployment_stage

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.deployment_stage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentStages:
    import capo_sagemaker.types.deployment_stage

    out: DeploymentStages = []
    for item in data:
        out.append(capo_sagemaker.types.deployment_stage.deserialize_aws_json_1_1(item))
    return out
