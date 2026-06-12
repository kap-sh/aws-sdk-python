"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentModelConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_deployment_model_config

EdgeDeploymentModelConfigs: TypeAlias = list[
    "aws_sdk_sagemaker.types.edge_deployment_model_config.EdgeDeploymentModelConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentModelConfigs) -> list:
    import aws_sdk_sagemaker.types.edge_deployment_model_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.edge_deployment_model_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeDeploymentModelConfigs:
    import aws_sdk_sagemaker.types.edge_deployment_model_config

    out: EdgeDeploymentModelConfigs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.edge_deployment_model_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
