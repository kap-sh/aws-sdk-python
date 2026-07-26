"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.rule_state

RuleStateList: TypeAlias = list["capo_codepipeline.types.rule_state.RuleState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleStateList) -> list:
    import capo_codepipeline.types.rule_state

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.rule_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleStateList:
    import capo_codepipeline.types.rule_state

    out: RuleStateList = []
    for item in data:
        out.append(capo_codepipeline.types.rule_state.deserialize_aws_json_1_1(item))
    return out
