"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatelessRuleGroupReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.stateless_rule_group_reference

StatelessRuleGroupReferences: TypeAlias = list[
    "aws_sdk_network_firewall.types.stateless_rule_group_reference.StatelessRuleGroupReference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatelessRuleGroupReferences) -> list:
    import aws_sdk_network_firewall.types.stateless_rule_group_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.stateless_rule_group_reference.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StatelessRuleGroupReferences:
    import aws_sdk_network_firewall.types.stateless_rule_group_reference

    out: StatelessRuleGroupReferences = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.stateless_rule_group_reference.deserialize_aws_json_1_0(
                item
            )
        )
    return out
