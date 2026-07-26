"""Generated from Smithy shape ``com.amazonaws.evs#RouteServerPeeringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.route_server_peering

RouteServerPeeringList: TypeAlias = list[
    "capo_evs.types.route_server_peering.RouteServerPeering"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RouteServerPeeringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RouteServerPeeringList:
    return list(data)
