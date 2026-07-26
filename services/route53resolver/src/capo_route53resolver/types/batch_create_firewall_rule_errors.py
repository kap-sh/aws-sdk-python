"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchCreateFirewallRuleErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.batch_create_firewall_rule_error

BatchCreateFirewallRuleErrors: TypeAlias = list[
    "capo_route53resolver.types.batch_create_firewall_rule_error.BatchCreateFirewallRuleError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateFirewallRuleErrors) -> list:
    import capo_route53resolver.types.batch_create_firewall_rule_error

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.batch_create_firewall_rule_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchCreateFirewallRuleErrors:
    import capo_route53resolver.types.batch_create_firewall_rule_error

    out: BatchCreateFirewallRuleErrors = []
    for item in data:
        out.append(
            capo_route53resolver.types.batch_create_firewall_rule_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
