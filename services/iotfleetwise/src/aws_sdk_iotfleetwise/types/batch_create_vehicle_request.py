"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#BatchCreateVehicleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.create_vehicle_request_items


class BatchCreateVehicleRequest(TypedDict):
    vehicles: "aws_sdk_iotfleetwise.types.create_vehicle_request_items.createVehicleRequestItems"
    """<p> A list of information about each vehicle to create. For more information, see the API data type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateVehicleRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.create_vehicle_request_items

    out["vehicles"] = (
        aws_sdk_iotfleetwise.types.create_vehicle_request_items.serialize_aws_json_1_0(
            value["vehicles"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateVehicleRequest:
    out: BatchCreateVehicleRequest = {}  # type: ignore[typeddict-item]
    if "vehicles" in data:
        import aws_sdk_iotfleetwise.types.create_vehicle_request_items

        out["vehicles"] = (
            aws_sdk_iotfleetwise.types.create_vehicle_request_items.deserialize_aws_json_1_0(
                data["vehicles"]
            )
        )
    else:
        raise DeserializationError("BatchCreateVehicleRequest.vehicles required")
    return out
