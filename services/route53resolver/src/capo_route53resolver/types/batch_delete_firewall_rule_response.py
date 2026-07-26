"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchDeleteFirewallRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.batch_delete_firewall_rule_errors
    import capo_route53resolver.types.firewall_rules


class BatchDeleteFirewallRuleResponse(TypedDict, closed=True):
    deleted_firewall_rules: NotRequired[
        "capo_route53resolver.types.firewall_rules.FirewallRules"
    ]
    """<p>The firewall rules that were successfully deleted by the request.</p>"""
    delete_errors: NotRequired[
        "capo_route53resolver.types.batch_delete_firewall_rule_errors.BatchDeleteFirewallRuleErrors"
    ]
    """<p>A list of errors that occurred while deleting the firewall rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFirewallRuleResponse) -> dict:
    out: dict = {}
    if "deleted_firewall_rules" in value:
        import capo_route53resolver.types.firewall_rules

        out["DeletedFirewallRules"] = (
            capo_route53resolver.types.firewall_rules.serialize_aws_json_1_1(
                value["deleted_firewall_rules"]
            )
        )
    if "delete_errors" in value:
        import capo_route53resolver.types.batch_delete_firewall_rule_errors

        out["DeleteErrors"] = (
            capo_route53resolver.types.batch_delete_firewall_rule_errors.serialize_aws_json_1_1(
                value["delete_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteFirewallRuleResponse:
    out: BatchDeleteFirewallRuleResponse = {}  # type: ignore[typeddict-item]
    if "DeletedFirewallRules" in data:
        import capo_route53resolver.types.firewall_rules

        out["deleted_firewall_rules"] = (
            capo_route53resolver.types.firewall_rules.deserialize_aws_json_1_1(
                data["DeletedFirewallRules"]
            )
        )
    if "DeleteErrors" in data:
        import capo_route53resolver.types.batch_delete_firewall_rule_errors

        out["delete_errors"] = (
            capo_route53resolver.types.batch_delete_firewall_rule_errors.deserialize_aws_json_1_1(
                data["DeleteErrors"]
            )
        )
    return out
