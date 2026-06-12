"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer

RuleGroupSourceStatelessRuleMatchAttributesProtocolsList: TypeAlias = list[
    "aws_sdk_securityhub.types.integer.Integer"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesProtocolsList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesProtocolsList:
    return list(data)
