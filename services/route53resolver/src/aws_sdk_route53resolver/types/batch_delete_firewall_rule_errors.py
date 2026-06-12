"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchDeleteFirewallRuleErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.batch_delete_firewall_rule_error

BatchDeleteFirewallRuleErrors: TypeAlias = list[
    "aws_sdk_route53resolver.types.batch_delete_firewall_rule_error.BatchDeleteFirewallRuleError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFirewallRuleErrors) -> list:
    import aws_sdk_route53resolver.types.batch_delete_firewall_rule_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.batch_delete_firewall_rule_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteFirewallRuleErrors:
    import aws_sdk_route53resolver.types.batch_delete_firewall_rule_error

    out: BatchDeleteFirewallRuleErrors = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.batch_delete_firewall_rule_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
