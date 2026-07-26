"""Generated from Smithy shape ``com.amazonaws.wafv2#FirewallManagerStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.managed_rule_group_statement
    import capo_wafv2.types.rule_group_reference_statement


class FirewallManagerStatement(TypedDict, closed=True):
    managed_rule_group_statement: NotRequired[
        "capo_wafv2.types.managed_rule_group_statement.ManagedRuleGroupStatement"
    ]
    """<p>A statement used by Firewall Manager to run the rules that are defined in a managed rule group. This is managed by Firewall Manager for an Firewall Manager WAF policy.</p>"""
    rule_group_reference_statement: NotRequired[
        "capo_wafv2.types.rule_group_reference_statement.RuleGroupReferenceStatement"
    ]
    """<p>A statement used by Firewall Manager to run the rules that are defined in a rule group. This is managed by Firewall Manager for an Firewall Manager WAF policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallManagerStatement) -> dict:
    out: dict = {}
    if "managed_rule_group_statement" in value:
        import capo_wafv2.types.managed_rule_group_statement

        out["ManagedRuleGroupStatement"] = (
            capo_wafv2.types.managed_rule_group_statement.serialize_aws_json_1_1(
                value["managed_rule_group_statement"]
            )
        )
    if "rule_group_reference_statement" in value:
        import capo_wafv2.types.rule_group_reference_statement

        out["RuleGroupReferenceStatement"] = (
            capo_wafv2.types.rule_group_reference_statement.serialize_aws_json_1_1(
                value["rule_group_reference_statement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallManagerStatement:
    out: FirewallManagerStatement = {}  # type: ignore[typeddict-item]
    if "ManagedRuleGroupStatement" in data:
        import capo_wafv2.types.managed_rule_group_statement

        out["managed_rule_group_statement"] = (
            capo_wafv2.types.managed_rule_group_statement.deserialize_aws_json_1_1(
                data["ManagedRuleGroupStatement"]
            )
        )
    if "RuleGroupReferenceStatement" in data:
        import capo_wafv2.types.rule_group_reference_statement

        out["rule_group_reference_statement"] = (
            capo_wafv2.types.rule_group_reference_statement.deserialize_aws_json_1_1(
                data["RuleGroupReferenceStatement"]
            )
        )
    return out
