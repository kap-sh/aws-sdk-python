"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VpcEndpointIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.vpc_endpoint_id

VpcEndpointIdList: TypeAlias = list[
    "capo_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> VpcEndpointIdList:
    return list(data)
