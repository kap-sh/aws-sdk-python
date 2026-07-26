"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_error

VpcEndpointErrorList: TypeAlias = list[
    "capo_opensearch.types.vpc_endpoint_error.VpcEndpointError"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointErrorList) -> list:
    import capo_opensearch.types.vpc_endpoint_error

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.vpc_endpoint_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> VpcEndpointErrorList:
    import capo_opensearch.types.vpc_endpoint_error

    out: VpcEndpointErrorList = []
    for item in data:
        out.append(capo_opensearch.types.vpc_endpoint_error.deserialize_json(item))
    return out
