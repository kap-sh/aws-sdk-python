"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.action_state

ActionStateList: TypeAlias = list["capo_codepipeline.types.action_state.ActionState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionStateList) -> list:
    import capo_codepipeline.types.action_state

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.action_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActionStateList:
    import capo_codepipeline.types.action_state

    out: ActionStateList = []
    for item in data:
        out.append(capo_codepipeline.types.action_state.deserialize_aws_json_1_1(item))
    return out
