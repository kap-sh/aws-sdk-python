"""Generated from Smithy shape ``com.amazonaws.deadline#FleetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_id

FleetIds: TypeAlias = list["capo_deadline.types.fleet_id.FleetId"]


# --- restJson1 ser/de ---
def serialize_json(value: FleetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> FleetIds:
    return list(data)
