"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_info

DeploymentsInfoList: TypeAlias = list[
    "aws_sdk_codedeploy.types.deployment_info.DeploymentInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentsInfoList) -> list:
    import aws_sdk_codedeploy.types.deployment_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.deployment_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentsInfoList:
    import aws_sdk_codedeploy.types.deployment_info

    out: DeploymentsInfoList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.deployment_info.deserialize_aws_json_1_1(item)
        )
    return out
