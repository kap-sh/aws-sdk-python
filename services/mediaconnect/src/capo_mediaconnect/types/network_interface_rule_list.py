"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NetworkInterfaceRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_router_network_interface_rule

NetworkInterfaceRuleList: TypeAlias = list[
    "capo_mediaconnect.types.public_router_network_interface_rule.PublicRouterNetworkInterfaceRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceRuleList) -> list:
    import capo_mediaconnect.types.public_router_network_interface_rule

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.public_router_network_interface_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkInterfaceRuleList:
    import capo_mediaconnect.types.public_router_network_interface_rule

    out: NetworkInterfaceRuleList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.public_router_network_interface_rule.deserialize_json(
                item
            )
        )
    return out
