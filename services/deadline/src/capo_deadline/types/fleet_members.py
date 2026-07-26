"""Generated from Smithy shape ``com.amazonaws.deadline#FleetMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_member

FleetMembers: TypeAlias = list["capo_deadline.types.fleet_member.FleetMember"]


# --- restJson1 ser/de ---
def serialize_json(value: FleetMembers) -> list:
    import capo_deadline.types.fleet_member

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetMembers:
    import capo_deadline.types.fleet_member

    out: FleetMembers = []
    for item in data:
        out.append(capo_deadline.types.fleet_member.deserialize_json(item))
    return out
