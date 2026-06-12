"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployActionExecutionTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.deploy_action_execution_target

DeployActionExecutionTargetList: TypeAlias = list[
    "aws_sdk_codepipeline.types.deploy_action_execution_target.DeployActionExecutionTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployActionExecutionTargetList) -> list:
    import aws_sdk_codepipeline.types.deploy_action_execution_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.deploy_action_execution_target.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeployActionExecutionTargetList:
    import aws_sdk_codepipeline.types.deploy_action_execution_target

    out: DeployActionExecutionTargetList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.deploy_action_execution_target.deserialize_aws_json_1_1(
                item
            )
        )
    return out
