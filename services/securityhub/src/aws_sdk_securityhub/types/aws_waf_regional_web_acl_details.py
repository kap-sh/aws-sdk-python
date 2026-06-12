"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalWebAclDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalWebAclDetails(TypedDict):
    default_action: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The action to perform if none of the rules contained in the web ACL match. </p>"""
    metric_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A name for the metrics for this web ACL. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A descriptive name for the web ACL. </p>"""
    rules_list: NotRequired[
        "aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list.AwsWafRegionalWebAclRulesList"
    ]
    """<p>An array that contains the action for each rule in a web ACL, the priority of the rule, and the ID of the rule. </p>"""
    web_acl_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the web ACL. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalWebAclDetails) -> dict:
    out: dict = {}
    if "default_action" in value:
        out["DefaultAction"] = value["default_action"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "rules_list" in value:
        import aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list

        out["RulesList"] = (
            aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list.serialize_json(
                value["rules_list"]
            )
        )
    if "web_acl_id" in value:
        out["WebAclId"] = value["web_acl_id"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalWebAclDetails:
    out: AwsWafRegionalWebAclDetails = {}  # type: ignore[typeddict-item]
    if "DefaultAction" in data:
        out["default_action"] = data["DefaultAction"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RulesList" in data:
        import aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list

        out["rules_list"] = (
            aws_sdk_securityhub.types.aws_waf_regional_web_acl_rules_list.deserialize_json(
                data["RulesList"]
            )
        )
    if "WebAclId" in data:
        out["web_acl_id"] = data["WebAclId"]
    return out
