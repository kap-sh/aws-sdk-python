"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NetworkInterfaceRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.public_router_network_interface_rule

NetworkInterfaceRuleList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.public_router_network_interface_rule.PublicRouterNetworkInterfaceRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceRuleList) -> list:
    import aws_sdk_mediaconnect.types.public_router_network_interface_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.public_router_network_interface_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkInterfaceRuleList:
    import aws_sdk_mediaconnect.types.public_router_network_interface_rule

    out: NetworkInterfaceRuleList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.public_router_network_interface_rule.deserialize_json(
                item
            )
        )
    return out
