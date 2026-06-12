"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_target

DeploymentTargetList: TypeAlias = list[
    "aws_sdk_codedeploy.types.deployment_target.DeploymentTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTargetList) -> list:
    import aws_sdk_codedeploy.types.deployment_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.deployment_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentTargetList:
    import aws_sdk_codedeploy.types.deployment_target

    out: DeploymentTargetList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.deployment_target.deserialize_aws_json_1_1(item)
        )
    return out
