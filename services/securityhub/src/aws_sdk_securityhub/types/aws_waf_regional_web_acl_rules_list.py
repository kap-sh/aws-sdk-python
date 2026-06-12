"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalWebAclRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list_details

AwsWafRegionalWebAclRulesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list_details.AwsWafRegionalWebAclRulesListDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalWebAclRulesList) -> list:
    import aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRegionalWebAclRulesList:
    import aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list_details

    out: AwsWafRegionalWebAclRulesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list_details.deserialize_json(
                item
            )
        )
    return out
