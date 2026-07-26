"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.vehicle_status

VehicleStatusList: TypeAlias = list[
    "capo_iotfleetwise.types.vehicle_status.VehicleStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleStatusList) -> list:
    import capo_iotfleetwise.types.vehicle_status

    out: list = []
    for item in value:
        out.append(capo_iotfleetwise.types.vehicle_status.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VehicleStatusList:
    import capo_iotfleetwise.types.vehicle_status

    out: VehicleStatusList = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.vehicle_status.deserialize_aws_json_1_0(item)
        )
    return out
