"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#updateVehicleErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.update_vehicle_error

updateVehicleErrors: TypeAlias = list[
    "capo_iotfleetwise.types.update_vehicle_error.UpdateVehicleError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: updateVehicleErrors) -> list:
    import capo_iotfleetwise.types.update_vehicle_error

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.update_vehicle_error.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> updateVehicleErrors:
    import capo_iotfleetwise.types.update_vehicle_error

    out: updateVehicleErrors = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.update_vehicle_error.deserialize_aws_json_1_0(item)
        )
    return out
