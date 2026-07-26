"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Flows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.flow

Flows: TypeAlias = list["capo_network_firewall.types.flow.Flow"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Flows) -> list:
    import capo_network_firewall.types.flow

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.flow.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Flows:
    import capo_network_firewall.types.flow

    out: Flows = []
    for item in data:
        out.append(capo_network_firewall.types.flow.deserialize_aws_json_1_0(item))
    return out
