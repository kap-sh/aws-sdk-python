"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2WebAclDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_rules_list
    import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details
    import aws_sdk_securityhub.types.aws_wafv2_web_acl_action_details
    import aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafv2WebAclDetails(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the web ACL. </p>"""
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource. </p>"""
    managedby_firewall_manager: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether this web ACL is managed by Firewall Manager. </p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A unique identifier for the web ACL. </p>"""
    capacity: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p> The web ACL capacity units (WCUs) currently being used by this web ACL. </p>"""
    captcha_config: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_details.AwsWafv2WebAclCaptchaConfigDetails"
    ]
    """<p> Specifies how WAF should handle CAPTCHA evaluations for rules that don't have their own <code>CaptchaConfig</code> settings. </p>"""
    default_action: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_web_acl_action_details.AwsWafv2WebAclActionDetails"
    ]
    """<p> The action to perform if none of the Rules contained in the web ACL match. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A description of the web ACL that helps with identification. </p>"""
    rules: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_rules_list.AwsWafv2RulesList"
    ]
    """<p> The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.AwsWafv2VisibilityConfigDetails"
    ]
    """<p> Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2WebAclDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "managedby_firewall_manager" in value:
        out["ManagedbyFirewallManager"] = value["managedby_firewall_manager"]
    if "id" in value:
        out["Id"] = value["id"]
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "captcha_config" in value:
        import aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_details

        out["CaptchaConfig"] = (
            aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_details.serialize_json(
                value["captcha_config"]
            )
        )
    if "default_action" in value:
        import aws_sdk_securityhub.types.aws_wafv2_web_acl_action_details

        out["DefaultAction"] = (
            aws_sdk_securityhub.types.aws_wafv2_web_acl_action_details.serialize_json(
                value["default_action"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import aws_sdk_securityhub.types.aws_wafv2_rules_list

        out["Rules"] = aws_sdk_securityhub.types.aws_wafv2_rules_list.serialize_json(
            value["rules"]
        )
    if "visibility_config" in value:
        import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details

        out["VisibilityConfig"] = (
            aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.serialize_json(
                value["visibility_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2WebAclDetails:
    out: AwsWafv2WebAclDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ManagedbyFirewallManager" in data:
        out["managedby_firewall_manager"] = data["ManagedbyFirewallManager"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    if "CaptchaConfig" in data:
        import aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_details

        out["captcha_config"] = (
            aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_details.deserialize_json(
                data["CaptchaConfig"]
            )
        )
    if "DefaultAction" in data:
        import aws_sdk_securityhub.types.aws_wafv2_web_acl_action_details

        out["default_action"] = (
            aws_sdk_securityhub.types.aws_wafv2_web_acl_action_details.deserialize_json(
                data["DefaultAction"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import aws_sdk_securityhub.types.aws_wafv2_rules_list

        out["rules"] = aws_sdk_securityhub.types.aws_wafv2_rules_list.deserialize_json(
            data["Rules"]
        )
    if "VisibilityConfig" in data:
        import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details

        out["visibility_config"] = (
            aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.deserialize_json(
                data["VisibilityConfig"]
            )
        )
    return out
