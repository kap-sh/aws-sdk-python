"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RuleNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.rule_name

RuleNameList: TypeAlias = list["capo_cloudwatch_events.types.rule_name.RuleName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RuleNameList:
    return list(data)
