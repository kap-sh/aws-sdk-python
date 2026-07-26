"""Generated from Smithy shape ``com.amazonaws.osis#VpcEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.vpc_endpoint

VpcEndpointsList: TypeAlias = list["capo_osis.types.vpc_endpoint.VpcEndpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointsList) -> list:
    import capo_osis.types.vpc_endpoint

    out: list = []
    for item in value:
        out.append(capo_osis.types.vpc_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> VpcEndpointsList:
    import capo_osis.types.vpc_endpoint

    out: VpcEndpointsList = []
    for item in data:
        out.append(capo_osis.types.vpc_endpoint.deserialize_json(item))
    return out
