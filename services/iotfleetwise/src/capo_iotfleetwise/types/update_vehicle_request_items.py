"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#updateVehicleRequestItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.update_vehicle_request_item

updateVehicleRequestItems: TypeAlias = list[
    "capo_iotfleetwise.types.update_vehicle_request_item.UpdateVehicleRequestItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: updateVehicleRequestItems) -> list:
    import capo_iotfleetwise.types.update_vehicle_request_item

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.update_vehicle_request_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> updateVehicleRequestItems:
    import capo_iotfleetwise.types.update_vehicle_request_item

    out: updateVehicleRequestItems = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.update_vehicle_request_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
