"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchCreateFirewallRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.batch_create_firewall_rule_errors
    import aws_sdk_route53resolver.types.firewall_rules


class BatchCreateFirewallRuleResponse(TypedDict, closed=True):
    created_firewall_rules: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rules.FirewallRules"
    ]
    """<p>The firewall rules that were successfully created by the request.</p>"""
    create_errors: NotRequired[
        "aws_sdk_route53resolver.types.batch_create_firewall_rule_errors.BatchCreateFirewallRuleErrors"
    ]
    """<p>A list of errors that occurred while creating the firewall rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateFirewallRuleResponse) -> dict:
    out: dict = {}
    if "created_firewall_rules" in value:
        import aws_sdk_route53resolver.types.firewall_rules

        out["CreatedFirewallRules"] = (
            aws_sdk_route53resolver.types.firewall_rules.serialize_aws_json_1_1(
                value["created_firewall_rules"]
            )
        )
    if "create_errors" in value:
        import aws_sdk_route53resolver.types.batch_create_firewall_rule_errors

        out["CreateErrors"] = (
            aws_sdk_route53resolver.types.batch_create_firewall_rule_errors.serialize_aws_json_1_1(
                value["create_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreateFirewallRuleResponse:
    out: BatchCreateFirewallRuleResponse = {}  # type: ignore[typeddict-item]
    if "CreatedFirewallRules" in data:
        import aws_sdk_route53resolver.types.firewall_rules

        out["created_firewall_rules"] = (
            aws_sdk_route53resolver.types.firewall_rules.deserialize_aws_json_1_1(
                data["CreatedFirewallRules"]
            )
        )
    if "CreateErrors" in data:
        import aws_sdk_route53resolver.types.batch_create_firewall_rule_errors

        out["create_errors"] = (
            aws_sdk_route53resolver.types.batch_create_firewall_rule_errors.deserialize_aws_json_1_1(
                data["CreateErrors"]
            )
        )
    return out
