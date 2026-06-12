"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.rule_option

RuleOptions: TypeAlias = list["aws_sdk_network_firewall.types.rule_option.RuleOption"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleOptions) -> list:
    import aws_sdk_network_firewall.types.rule_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.rule_option.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleOptions:
    import aws_sdk_network_firewall.types.rule_option

    out: RuleOptions = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.rule_option.deserialize_aws_json_1_0(item)
        )
    return out
