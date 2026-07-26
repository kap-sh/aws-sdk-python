"""Generated from Smithy shape ``com.amazonaws.wafregional#ExcludedRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.excluded_rule

ExcludedRules: TypeAlias = list["capo_waf_regional.types.excluded_rule.ExcludedRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludedRules) -> list:
    import capo_waf_regional.types.excluded_rule

    out: list = []
    for item in value:
        out.append(capo_waf_regional.types.excluded_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExcludedRules:
    import capo_waf_regional.types.excluded_rule

    out: ExcludedRules = []
    for item in data:
        out.append(capo_waf_regional.types.excluded_rule.deserialize_aws_json_1_1(item))
    return out
