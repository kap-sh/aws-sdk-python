"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.rule

RuleList: TypeAlias = list["capo_frauddetector.types.rule.Rule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleList) -> list:
    import capo_frauddetector.types.rule

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleList:
    import capo_frauddetector.types.rule

    out: RuleList = []
    for item in data:
        out.append(capo_frauddetector.types.rule.deserialize_aws_json_1_1(item))
    return out
