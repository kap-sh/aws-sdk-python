"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#createVehicleResponses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.create_vehicle_response_item

createVehicleResponses: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.create_vehicle_response_item.CreateVehicleResponseItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: createVehicleResponses) -> list:
    import aws_sdk_iotfleetwise.types.create_vehicle_response_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.create_vehicle_response_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> createVehicleResponses:
    import aws_sdk_iotfleetwise.types.create_vehicle_response_item

    out: createVehicleResponses = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.create_vehicle_response_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
