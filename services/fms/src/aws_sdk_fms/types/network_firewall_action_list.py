"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.network_firewall_action

NetworkFirewallActionList: TypeAlias = list[
    "aws_sdk_fms.types.network_firewall_action.NetworkFirewallAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallActionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NetworkFirewallActionList:
    return list(data)
