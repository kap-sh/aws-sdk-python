"""Generated from Smithy shape ``com.amazonaws.eventbridge#RuleResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.rule

RuleResponseList: TypeAlias = list["capo_eventbridge.types.rule.Rule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleResponseList) -> list:
    import capo_eventbridge.types.rule

    out: list = []
    for item in value:
        out.append(capo_eventbridge.types.rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleResponseList:
    import capo_eventbridge.types.rule

    out: RuleResponseList = []
    for item in data:
        out.append(capo_eventbridge.types.rule.deserialize_aws_json_1_1(item))
    return out
