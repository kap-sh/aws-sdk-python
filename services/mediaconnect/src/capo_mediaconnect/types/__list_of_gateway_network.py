"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfGatewayNetwork``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.gateway_network

__listOfGatewayNetwork: TypeAlias = list[
    "capo_mediaconnect.types.gateway_network.GatewayNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGatewayNetwork) -> list:
    import capo_mediaconnect.types.gateway_network

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.gateway_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfGatewayNetwork:
    import capo_mediaconnect.types.gateway_network

    out: __listOfGatewayNetwork = []
    for item in data:
        out.append(capo_mediaconnect.types.gateway_network.deserialize_json(item))
    return out
