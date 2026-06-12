"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2RulesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_rules_action_details
    import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafv2RulesDetails(TypedDict):
    action: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_rules_action_details.AwsWafv2RulesActionDetails"
    ]
    """<p> The action that WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the rule. </p>"""
    override_action: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The action to use in the place of the action that results from the rule group evaluation. </p>"""
    priority: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> If you define more than one Rule in a WebACL, WAF evaluates each request against the Rules in order based on the value of <code>Priority</code>. WAF processes rules with lower priority first. The priorities don't need to be consecutive, but they must all be different. </p>"""
    visibility_config: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.AwsWafv2VisibilityConfigDetails"
    ]
    """<p> Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2RulesDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_securityhub.types.aws_wafv2_rules_action_details

        out["Action"] = (
            aws_sdk_securityhub.types.aws_wafv2_rules_action_details.serialize_json(
                value["action"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "override_action" in value:
        out["OverrideAction"] = value["override_action"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "visibility_config" in value:
        import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details

        out["VisibilityConfig"] = (
            aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.serialize_json(
                value["visibility_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2RulesDetails:
    out: AwsWafv2RulesDetails = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_securityhub.types.aws_wafv2_rules_action_details

        out["action"] = (
            aws_sdk_securityhub.types.aws_wafv2_rules_action_details.deserialize_json(
                data["Action"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "OverrideAction" in data:
        out["override_action"] = data["OverrideAction"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "VisibilityConfig" in data:
        import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details

        out["visibility_config"] = (
            aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.deserialize_json(
                data["VisibilityConfig"]
            )
        )
    return out
