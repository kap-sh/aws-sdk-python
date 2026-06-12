"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleActionOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.rule_action_override

RuleActionOverrides: TypeAlias = list[
    "aws_sdk_wafv2.types.rule_action_override.RuleActionOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleActionOverrides) -> list:
    import aws_sdk_wafv2.types.rule_action_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wafv2.types.rule_action_override.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RuleActionOverrides:
    import aws_sdk_wafv2.types.rule_action_override

    out: RuleActionOverrides = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.rule_action_override.deserialize_aws_json_1_1(item)
        )
    return out
