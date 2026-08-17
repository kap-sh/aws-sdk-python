"""Generated from Smithy shape ``com.amazonaws.eventbridge#RuleNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.rule_name

RuleNameList: TypeAlias = list["capo_eventbridge.types.rule_name.RuleName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RuleNameList:
    return [item for item in data if item is not None]
