"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.stage_state

StageStateList: TypeAlias = list["capo_codepipeline.types.stage_state.StageState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageStateList) -> list:
    import capo_codepipeline.types.stage_state

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.stage_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StageStateList:
    import capo_codepipeline.types.stage_state

    out: StageStateList = []
    for item in data:
        out.append(capo_codepipeline.types.stage_state.deserialize_aws_json_1_1(item))
    return out
