"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_string_value

RuleStringList: TypeAlias = list[
    "aws_sdk_mailmanager.types.rule_string_value.RuleStringValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RuleStringList:
    return list(data)
