"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchUpdateFirewallRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.batch_update_firewall_rule_errors
    import capo_route53resolver.types.firewall_rules


class BatchUpdateFirewallRuleResponse(TypedDict, closed=True):
    updated_firewall_rules: NotRequired[
        "capo_route53resolver.types.firewall_rules.FirewallRules"
    ]
    """<p>The firewall rules that were successfully updated by the request.</p>"""
    update_errors: NotRequired[
        "capo_route53resolver.types.batch_update_firewall_rule_errors.BatchUpdateFirewallRuleErrors"
    ]
    """<p>A list of errors that occurred while updating the firewall rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateFirewallRuleResponse) -> dict:
    out: dict = {}
    if "updated_firewall_rules" in value:
        import capo_route53resolver.types.firewall_rules

        out["UpdatedFirewallRules"] = (
            capo_route53resolver.types.firewall_rules.serialize_aws_json_1_1(
                value["updated_firewall_rules"]
            )
        )
    if "update_errors" in value:
        import capo_route53resolver.types.batch_update_firewall_rule_errors

        out["UpdateErrors"] = (
            capo_route53resolver.types.batch_update_firewall_rule_errors.serialize_aws_json_1_1(
                value["update_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateFirewallRuleResponse:
    out: BatchUpdateFirewallRuleResponse = {}  # type: ignore[typeddict-item]
    if "UpdatedFirewallRules" in data:
        import capo_route53resolver.types.firewall_rules

        out["updated_firewall_rules"] = (
            capo_route53resolver.types.firewall_rules.deserialize_aws_json_1_1(
                data["UpdatedFirewallRules"]
            )
        )
    if "UpdateErrors" in data:
        import capo_route53resolver.types.batch_update_firewall_rule_errors

        out["update_errors"] = (
            capo_route53resolver.types.batch_update_firewall_rule_errors.deserialize_aws_json_1_1(
                data["UpdateErrors"]
            )
        )
    return out
