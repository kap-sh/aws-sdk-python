"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.evaluated_rule

EvaluatedRuleList: TypeAlias = list[
    "aws_sdk_frauddetector.types.evaluated_rule.EvaluatedRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedRuleList) -> list:
    import aws_sdk_frauddetector.types.evaluated_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.evaluated_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EvaluatedRuleList:
    import aws_sdk_frauddetector.types.evaluated_rule

    out: EvaluatedRuleList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.evaluated_rule.deserialize_aws_json_1_1(item)
        )
    return out
