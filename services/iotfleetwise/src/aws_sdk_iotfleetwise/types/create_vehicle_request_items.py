"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#createVehicleRequestItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.create_vehicle_request_item

createVehicleRequestItems: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.create_vehicle_request_item.CreateVehicleRequestItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: createVehicleRequestItems) -> list:
    import aws_sdk_iotfleetwise.types.create_vehicle_request_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.create_vehicle_request_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> createVehicleRequestItems:
    import aws_sdk_iotfleetwise.types.create_vehicle_request_item

    out: createVehicleRequestItems = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.create_vehicle_request_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
