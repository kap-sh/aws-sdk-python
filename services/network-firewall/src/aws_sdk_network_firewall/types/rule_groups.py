"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.rule_group_metadata

RuleGroups: TypeAlias = list[
    "aws_sdk_network_firewall.types.rule_group_metadata.RuleGroupMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroups) -> list:
    import aws_sdk_network_firewall.types.rule_group_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.rule_group_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleGroups:
    import aws_sdk_network_firewall.types.rule_group_metadata

    out: RuleGroups = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.rule_group_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
