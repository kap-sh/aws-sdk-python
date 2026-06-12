"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatelessRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.stateless_rule

StatelessRules: TypeAlias = list[
    "aws_sdk_network_firewall.types.stateless_rule.StatelessRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatelessRules) -> list:
    import aws_sdk_network_firewall.types.stateless_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.stateless_rule.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StatelessRules:
    import aws_sdk_network_firewall.types.stateless_rule

    out: StatelessRules = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.stateless_rule.deserialize_aws_json_1_0(item)
        )
    return out
