"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.rule_execution_detail

RuleExecutionDetailList: TypeAlias = list[
    "capo_codepipeline.types.rule_execution_detail.RuleExecutionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionDetailList) -> list:
    import capo_codepipeline.types.rule_execution_detail

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.rule_execution_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RuleExecutionDetailList:
    import capo_codepipeline.types.rule_execution_detail

    out: RuleExecutionDetailList = []
    for item in data:
        out.append(
            capo_codepipeline.types.rule_execution_detail.deserialize_aws_json_1_1(item)
        )
    return out
