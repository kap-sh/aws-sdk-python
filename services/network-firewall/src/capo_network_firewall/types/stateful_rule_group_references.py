"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleGroupReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.stateful_rule_group_reference

StatefulRuleGroupReferences: TypeAlias = list[
    "capo_network_firewall.types.stateful_rule_group_reference.StatefulRuleGroupReference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleGroupReferences) -> list:
    import capo_network_firewall.types.stateful_rule_group_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.stateful_rule_group_reference.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StatefulRuleGroupReferences:
    import capo_network_firewall.types.stateful_rule_group_reference

    out: StatefulRuleGroupReferences = []
    for item in data:
        out.append(
            capo_network_firewall.types.stateful_rule_group_reference.deserialize_aws_json_1_0(
                item
            )
        )
    return out
