"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchUpdateFirewallRuleErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.batch_update_firewall_rule_error

BatchUpdateFirewallRuleErrors: TypeAlias = list[
    "aws_sdk_route53resolver.types.batch_update_firewall_rule_error.BatchUpdateFirewallRuleError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateFirewallRuleErrors) -> list:
    import aws_sdk_route53resolver.types.batch_update_firewall_rule_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.batch_update_firewall_rule_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchUpdateFirewallRuleErrors:
    import aws_sdk_route53resolver.types.batch_update_firewall_rule_error

    out: BatchUpdateFirewallRuleErrors = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.batch_update_firewall_rule_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
