"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_ip_string_value

RuleIpValueList: TypeAlias = list[
    "capo_mailmanager.types.rule_ip_string_value.RuleIpStringValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIpValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RuleIpValueList:
    return list(data)
