"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint

VpcEndpoints: TypeAlias = list["capo_opensearch.types.vpc_endpoint.VpcEndpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpoints) -> list:
    import capo_opensearch.types.vpc_endpoint

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.vpc_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> VpcEndpoints:
    import capo_opensearch.types.vpc_endpoint

    out: VpcEndpoints = []
    for item in data:
        out.append(capo_opensearch.types.vpc_endpoint.deserialize_json(item))
    return out
