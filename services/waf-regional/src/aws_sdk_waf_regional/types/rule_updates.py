"""Generated from Smithy shape ``com.amazonaws.wafregional#RuleUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.rule_update

RuleUpdates: TypeAlias = list["aws_sdk_waf_regional.types.rule_update.RuleUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleUpdates) -> list:
    import aws_sdk_waf_regional.types.rule_update

    out: list = []
    for item in value:
        out.append(aws_sdk_waf_regional.types.rule_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleUpdates:
    import aws_sdk_waf_regional.types.rule_update

    out: RuleUpdates = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.rule_update.deserialize_aws_json_1_1(item)
        )
    return out
