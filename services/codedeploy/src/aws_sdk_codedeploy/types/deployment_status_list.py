"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_status

DeploymentStatusList: TypeAlias = list[
    "aws_sdk_codedeploy.types.deployment_status.DeploymentStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStatusList) -> list:
    import aws_sdk_codedeploy.types.deployment_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.deployment_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentStatusList:
    import aws_sdk_codedeploy.types.deployment_status

    out: DeploymentStatusList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.deployment_status.deserialize_aws_json_1_1(item)
        )
    return out
