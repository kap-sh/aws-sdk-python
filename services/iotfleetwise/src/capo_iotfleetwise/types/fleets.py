"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#fleets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fleet_id

fleets: TypeAlias = list["capo_iotfleetwise.types.fleet_id.fleetId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: fleets) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> fleets:
    return list(data)
