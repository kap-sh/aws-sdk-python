"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.stateful_rule

StatefulRules: TypeAlias = list[
    "aws_sdk_network_firewall.types.stateful_rule.StatefulRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRules) -> list:
    import aws_sdk_network_firewall.types.stateful_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.stateful_rule.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StatefulRules:
    import aws_sdk_network_firewall.types.stateful_rule

    out: StatefulRules = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.stateful_rule.deserialize_aws_json_1_0(item)
        )
    return out
