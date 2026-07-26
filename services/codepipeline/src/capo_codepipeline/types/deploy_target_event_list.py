"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_target_event

DeployTargetEventList: TypeAlias = list[
    "capo_codepipeline.types.deploy_target_event.DeployTargetEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEventList) -> list:
    import capo_codepipeline.types.deploy_target_event

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.deploy_target_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeployTargetEventList:
    import capo_codepipeline.types.deploy_target_event

    out: DeployTargetEventList = []
    for item in data:
        out.append(
            capo_codepipeline.types.deploy_target_event.deserialize_aws_json_1_1(item)
        )
    return out
