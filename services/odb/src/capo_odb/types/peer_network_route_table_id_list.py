"""Generated from Smithy shape ``com.amazonaws.odb#PeerNetworkRouteTableIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.peer_network_route_table_id

PeerNetworkRouteTableIdList: TypeAlias = list[
    "capo_odb.types.peer_network_route_table_id.PeerNetworkRouteTableId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PeerNetworkRouteTableIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PeerNetworkRouteTableIdList:
    return list(data)
