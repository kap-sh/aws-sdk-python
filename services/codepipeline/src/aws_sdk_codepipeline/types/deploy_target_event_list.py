"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.deploy_target_event

DeployTargetEventList: TypeAlias = list[
    "aws_sdk_codepipeline.types.deploy_target_event.DeployTargetEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEventList) -> list:
    import aws_sdk_codepipeline.types.deploy_target_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.deploy_target_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeployTargetEventList:
    import aws_sdk_codepipeline.types.deploy_target_event

    out: DeployTargetEventList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.deploy_target_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out
