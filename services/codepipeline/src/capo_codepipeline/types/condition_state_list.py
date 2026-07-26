"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_state

ConditionStateList: TypeAlias = list[
    "capo_codepipeline.types.condition_state.ConditionState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionStateList) -> list:
    import capo_codepipeline.types.condition_state

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.condition_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConditionStateList:
    import capo_codepipeline.types.condition_state

    out: ConditionStateList = []
    for item in data:
        out.append(
            capo_codepipeline.types.condition_state.deserialize_aws_json_1_1(item)
        )
    return out
