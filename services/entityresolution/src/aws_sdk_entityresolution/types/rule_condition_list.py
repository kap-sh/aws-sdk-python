"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.rule_condition

RuleConditionList: TypeAlias = list[
    "aws_sdk_entityresolution.types.rule_condition.RuleCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleConditionList) -> list:
    import aws_sdk_entityresolution.types.rule_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.rule_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleConditionList:
    import aws_sdk_entityresolution.types.rule_condition

    out: RuleConditionList = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.rule_condition.deserialize_json(item))
    return out
