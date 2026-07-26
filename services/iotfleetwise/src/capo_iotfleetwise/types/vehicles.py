"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#vehicles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.vehicle_name

vehicles: TypeAlias = list["capo_iotfleetwise.types.vehicle_name.vehicleName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: vehicles) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> vehicles:
    return list(data)
