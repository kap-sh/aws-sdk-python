"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CustomActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.custom_action

CustomActions: TypeAlias = list[
    "capo_network_firewall.types.custom_action.CustomAction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomActions) -> list:
    import capo_network_firewall.types.custom_action

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.custom_action.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CustomActions:
    import capo_network_firewall.types.custom_action

    out: CustomActions = []
    for item in data:
        out.append(
            capo_network_firewall.types.custom_action.deserialize_aws_json_1_0(item)
        )
    return out
