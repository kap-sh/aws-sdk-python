"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#updateVehicleResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.update_vehicle_response_item

updateVehicleResponseItems: TypeAlias = list[
    "capo_iotfleetwise.types.update_vehicle_response_item.UpdateVehicleResponseItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: updateVehicleResponseItems) -> list:
    import capo_iotfleetwise.types.update_vehicle_response_item

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.update_vehicle_response_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> updateVehicleResponseItems:
    import capo_iotfleetwise.types.update_vehicle_response_item

    out: updateVehicleResponseItems = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.update_vehicle_response_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
