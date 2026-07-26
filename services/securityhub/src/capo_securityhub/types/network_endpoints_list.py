"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.network_endpoint

NetworkEndpointsList: TypeAlias = list[
    "capo_securityhub.types.network_endpoint.NetworkEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkEndpointsList) -> list:
    import capo_securityhub.types.network_endpoint

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.network_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkEndpointsList:
    import capo_securityhub.types.network_endpoint

    out: NetworkEndpointsList = []
    for item in data:
        out.append(capo_securityhub.types.network_endpoint.deserialize_json(item))
    return out
