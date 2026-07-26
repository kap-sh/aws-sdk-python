"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.routing_profile_id

RoutingProfiles: TypeAlias = list[
    "capo_connect.types.routing_profile_id.RoutingProfileId"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfiles) -> list:
    return list(value)


def deserialize_json(data: list) -> RoutingProfiles:
    return list(data)
