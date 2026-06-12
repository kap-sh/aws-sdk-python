"""Generated from Smithy shape ``com.amazonaws.securityhub#WafExcludedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.waf_excluded_rule

WafExcludedRuleList: TypeAlias = list[
    "aws_sdk_securityhub.types.waf_excluded_rule.WafExcludedRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: WafExcludedRuleList) -> list:
    import aws_sdk_securityhub.types.waf_excluded_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.waf_excluded_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> WafExcludedRuleList:
    import aws_sdk_securityhub.types.waf_excluded_rule

    out: WafExcludedRuleList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.waf_excluded_rule.deserialize_json(item))
    return out
