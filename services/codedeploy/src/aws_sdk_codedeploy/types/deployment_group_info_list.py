"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentGroupInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_group_info

DeploymentGroupInfoList: TypeAlias = list[
    "aws_sdk_codedeploy.types.deployment_group_info.DeploymentGroupInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentGroupInfoList) -> list:
    import aws_sdk_codedeploy.types.deployment_group_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.deployment_group_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentGroupInfoList:
    import aws_sdk_codedeploy.types.deployment_group_info

    out: DeploymentGroupInfoList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.deployment_group_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
