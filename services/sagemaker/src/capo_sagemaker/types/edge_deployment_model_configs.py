"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentModelConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_deployment_model_config

EdgeDeploymentModelConfigs: TypeAlias = list[
    "capo_sagemaker.types.edge_deployment_model_config.EdgeDeploymentModelConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentModelConfigs) -> list:
    import capo_sagemaker.types.edge_deployment_model_config

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.edge_deployment_model_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeDeploymentModelConfigs:
    import capo_sagemaker.types.edge_deployment_model_config

    out: EdgeDeploymentModelConfigs = []
    for item in data:
        out.append(
            capo_sagemaker.types.edge_deployment_model_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
