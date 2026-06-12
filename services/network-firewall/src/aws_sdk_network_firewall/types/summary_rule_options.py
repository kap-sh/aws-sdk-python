"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SummaryRuleOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.summary_rule_option

SummaryRuleOptions: TypeAlias = list[
    "aws_sdk_network_firewall.types.summary_rule_option.SummaryRuleOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryRuleOptions) -> list:
    import aws_sdk_network_firewall.types.summary_rule_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.summary_rule_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SummaryRuleOptions:
    import aws_sdk_network_firewall.types.summary_rule_option

    out: SummaryRuleOptions = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.summary_rule_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
