"""Generated from Smithy shape ``com.amazonaws.securityagent#DiscoveredEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.discovered_endpoint

DiscoveredEndpointList: TypeAlias = list[
    "capo_securityagent.types.discovered_endpoint.DiscoveredEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredEndpointList) -> list:
    import capo_securityagent.types.discovered_endpoint

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.discovered_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> DiscoveredEndpointList:
    import capo_securityagent.types.discovered_endpoint

    out: DiscoveredEndpointList = []
    for item in data:
        out.append(capo_securityagent.types.discovered_endpoint.deserialize_json(item))
    return out
