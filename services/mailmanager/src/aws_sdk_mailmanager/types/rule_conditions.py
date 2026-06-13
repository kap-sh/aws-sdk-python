"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_condition

RuleConditions: TypeAlias = list[
    "aws_sdk_mailmanager.types.rule_condition.RuleCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleConditions) -> list:
    import aws_sdk_mailmanager.types.rule_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.rule_condition.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleConditions:
    import aws_sdk_mailmanager.types.rule_condition

    out: RuleConditions = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.rule_condition.deserialize_aws_json_1_0(item)
        )
    return out
