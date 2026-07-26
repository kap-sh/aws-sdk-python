"""Generated from Smithy shape ``com.amazonaws.osis#ServiceVpcEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.service_vpc_endpoint

ServiceVpcEndpointsList: TypeAlias = list[
    "capo_osis.types.service_vpc_endpoint.ServiceVpcEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceVpcEndpointsList) -> list:
    import capo_osis.types.service_vpc_endpoint

    out: list = []
    for item in value:
        out.append(capo_osis.types.service_vpc_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceVpcEndpointsList:
    import capo_osis.types.service_vpc_endpoint

    out: ServiceVpcEndpointsList = []
    for item in data:
        out.append(capo_osis.types.service_vpc_endpoint.deserialize_json(item))
    return out
