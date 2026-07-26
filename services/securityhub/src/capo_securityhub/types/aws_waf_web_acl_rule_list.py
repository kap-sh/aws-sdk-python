"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafWebAclRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_web_acl_rule

AwsWafWebAclRuleList: TypeAlias = list[
    "capo_securityhub.types.aws_waf_web_acl_rule.AwsWafWebAclRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafWebAclRuleList) -> list:
    import capo_securityhub.types.aws_waf_web_acl_rule

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_waf_web_acl_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsWafWebAclRuleList:
    import capo_securityhub.types.aws_waf_web_acl_rule

    out: AwsWafWebAclRuleList = []
    for item in data:
        out.append(capo_securityhub.types.aws_waf_web_acl_rule.deserialize_json(item))
    return out
