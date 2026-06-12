"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#createVehicleErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.create_vehicle_error

createVehicleErrors: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.create_vehicle_error.CreateVehicleError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: createVehicleErrors) -> list:
    import aws_sdk_iotfleetwise.types.create_vehicle_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.create_vehicle_error.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> createVehicleErrors:
    import aws_sdk_iotfleetwise.types.create_vehicle_error

    out: createVehicleErrors = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.create_vehicle_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
