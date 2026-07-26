"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_info

DeploymentsInfoList: TypeAlias = list[
    "capo_codedeploy.types.deployment_info.DeploymentInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentsInfoList) -> list:
    import capo_codedeploy.types.deployment_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.deployment_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentsInfoList:
    import capo_codedeploy.types.deployment_info

    out: DeploymentsInfoList = []
    for item in data:
        out.append(capo_codedeploy.types.deployment_info.deserialize_aws_json_1_1(item))
    return out
