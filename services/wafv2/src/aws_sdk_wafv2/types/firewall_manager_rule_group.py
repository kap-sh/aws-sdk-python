"""Generated from Smithy shape ``com.amazonaws.wafv2#FirewallManagerRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.firewall_manager_statement
    import aws_sdk_wafv2.types.override_action
    import aws_sdk_wafv2.types.rule_priority
    import aws_sdk_wafv2.types.visibility_config


class FirewallManagerRuleGroup(TypedDict, closed=True):
    name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>"""
    priority: "aws_sdk_wafv2.types.rule_priority.RulePriority"
    """<p>If you define more than one rule group in the first or last Firewall Manager rule groups, WAF evaluates each request against the rule groups in order, starting from the lowest priority setting. The priorities don't need to be consecutive, but they must all be different.</p>"""
    firewall_manager_statement: (
        "aws_sdk_wafv2.types.firewall_manager_statement.FirewallManagerStatement"
    )
    """<p>The processing guidance for an Firewall Manager rule. This is like a regular rule <a>Statement</a>, but it can only contain a rule group reference.</p>"""
    override_action: "aws_sdk_wafv2.types.override_action.OverrideAction"
    """<p>The action to use in the place of the action that results from the rule group evaluation. Set the override action to none to leave the result of the rule group alone. Set it to count to override the result to count only. </p> <p>You can only use this for rule statements that reference a rule group, like <code>RuleGroupReferenceStatement</code> and <code>ManagedRuleGroupStatement</code>. </p> <note> <p>This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with <code>Count</code> action, in your rule group reference statement settings. </p> </note>"""
    visibility_config: "aws_sdk_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallManagerRuleGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Priority"] = value.get("priority", 0)
    import aws_sdk_wafv2.types.firewall_manager_statement

    out["FirewallManagerStatement"] = (
        aws_sdk_wafv2.types.firewall_manager_statement.serialize_aws_json_1_1(
            value["firewall_manager_statement"]
        )
    )
    import aws_sdk_wafv2.types.override_action

    out["OverrideAction"] = aws_sdk_wafv2.types.override_action.serialize_aws_json_1_1(
        value["override_action"]
    )
    import aws_sdk_wafv2.types.visibility_config

    out["VisibilityConfig"] = (
        aws_sdk_wafv2.types.visibility_config.serialize_aws_json_1_1(
            value["visibility_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallManagerRuleGroup:
    out: FirewallManagerRuleGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FirewallManagerRuleGroup.name required")
    if "Priority" in data:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if "FirewallManagerStatement" in data:
        import aws_sdk_wafv2.types.firewall_manager_statement

        out["firewall_manager_statement"] = (
            aws_sdk_wafv2.types.firewall_manager_statement.deserialize_aws_json_1_1(
                data["FirewallManagerStatement"]
            )
        )
    else:
        raise DeserializationError(
            "FirewallManagerRuleGroup.firewall_manager_statement required"
        )
    if "OverrideAction" in data:
        import aws_sdk_wafv2.types.override_action

        out["override_action"] = (
            aws_sdk_wafv2.types.override_action.deserialize_aws_json_1_1(
                data["OverrideAction"]
            )
        )
    else:
        raise DeserializationError("FirewallManagerRuleGroup.override_action required")
    if "VisibilityConfig" in data:
        import aws_sdk_wafv2.types.visibility_config

        out["visibility_config"] = (
            aws_sdk_wafv2.types.visibility_config.deserialize_aws_json_1_1(
                data["VisibilityConfig"]
            )
        )
    else:
        raise DeserializationError(
            "FirewallManagerRuleGroup.visibility_config required"
        )
    return out
