"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.network_endpoint

NetworkEndpoints: TypeAlias = list[
    "capo_guardduty.types.network_endpoint.NetworkEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkEndpoints) -> list:
    import capo_guardduty.types.network_endpoint

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.network_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkEndpoints:
    import capo_guardduty.types.network_endpoint

    out: NetworkEndpoints = []
    for item in data:
        out.append(capo_guardduty.types.network_endpoint.deserialize_json(item))
    return out
