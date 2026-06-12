"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.ip_set
    import aws_sdk_network_firewall.types.rule_variable_name

IPSets: TypeAlias = dict[
    "aws_sdk_network_firewall.types.rule_variable_name.RuleVariableName",
    "aws_sdk_network_firewall.types.ip_set.IPSet",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: IPSets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_network_firewall.types.ip_set

        out[key] = aws_sdk_network_firewall.types.ip_set.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSets:
    out: IPSets = {}
    for key, value in data.items():
        import aws_sdk_network_firewall.types.ip_set

        out[key] = aws_sdk_network_firewall.types.ip_set.deserialize_aws_json_1_0(value)
    return out
