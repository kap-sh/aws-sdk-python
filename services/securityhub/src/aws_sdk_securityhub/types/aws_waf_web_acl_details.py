"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafWebAclDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_web_acl_rule_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafWebAclDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A friendly name or description of the web ACL. You can't change the name of a web ACL after you create it.</p>"""
    default_action: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The action to perform if none of the rules contained in the web ACL match.</p>"""
    rules: NotRequired[
        "aws_sdk_securityhub.types.aws_waf_web_acl_rule_list.AwsWafWebAclRuleList"
    ]
    """<p>An array that contains the action for each rule in a web ACL, the priority of the rule, and the ID of the rule.</p>"""
    web_acl_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A unique identifier for a web ACL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafWebAclDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "default_action" in value:
        out["DefaultAction"] = value["default_action"]
    if "rules" in value:
        import aws_sdk_securityhub.types.aws_waf_web_acl_rule_list

        out["Rules"] = (
            aws_sdk_securityhub.types.aws_waf_web_acl_rule_list.serialize_json(
                value["rules"]
            )
        )
    if "web_acl_id" in value:
        out["WebAclId"] = value["web_acl_id"]
    return out


def deserialize_json(data: dict) -> AwsWafWebAclDetails:
    out: AwsWafWebAclDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DefaultAction" in data:
        out["default_action"] = data["DefaultAction"]
    if "Rules" in data:
        import aws_sdk_securityhub.types.aws_waf_web_acl_rule_list

        out["rules"] = (
            aws_sdk_securityhub.types.aws_waf_web_acl_rule_list.deserialize_json(
                data["Rules"]
            )
        )
    if "WebAclId" in data:
        out["web_acl_id"] = data["WebAclId"]
    return out
