"""Generated from Smithy shape ``com.amazonaws.wafregional#ActivatedRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.activated_rule

ActivatedRules: TypeAlias = list[
    "aws_sdk_waf_regional.types.activated_rule.ActivatedRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivatedRules) -> list:
    import aws_sdk_waf_regional.types.activated_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.activated_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ActivatedRules:
    import aws_sdk_waf_regional.types.activated_rule

    out: ActivatedRules = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.activated_rule.deserialize_aws_json_1_1(item)
        )
    return out
