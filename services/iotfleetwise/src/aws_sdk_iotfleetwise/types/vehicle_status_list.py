"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.vehicle_status

VehicleStatusList: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.vehicle_status.VehicleStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleStatusList) -> list:
    import aws_sdk_iotfleetwise.types.vehicle_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.vehicle_status.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VehicleStatusList:
    import aws_sdk_iotfleetwise.types.vehicle_status

    out: VehicleStatusList = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.vehicle_status.deserialize_aws_json_1_0(item)
        )
    return out
