"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#BatchUpdateVehicleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.update_vehicle_errors
    import aws_sdk_iotfleetwise.types.update_vehicle_response_items


class BatchUpdateVehicleResponse(TypedDict, closed=True):
    vehicles: NotRequired[
        "aws_sdk_iotfleetwise.types.update_vehicle_response_items.updateVehicleResponseItems"
    ]
    """<p> A list of information about the batch of updated vehicles. </p> <note> <p>This list contains only unique IDs for the vehicles that were updated.</p> </note>"""
    errors: NotRequired[
        "aws_sdk_iotfleetwise.types.update_vehicle_errors.updateVehicleErrors"
    ]
    """<p>A list of information about errors returned while updating a batch of vehicles, or, if there aren't any errors, an empty list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateVehicleResponse) -> dict:
    out: dict = {}
    if "vehicles" in value:
        import aws_sdk_iotfleetwise.types.update_vehicle_response_items

        out["vehicles"] = (
            aws_sdk_iotfleetwise.types.update_vehicle_response_items.serialize_aws_json_1_0(
                value["vehicles"]
            )
        )
    if "errors" in value:
        import aws_sdk_iotfleetwise.types.update_vehicle_errors

        out["errors"] = (
            aws_sdk_iotfleetwise.types.update_vehicle_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateVehicleResponse:
    out: BatchUpdateVehicleResponse = {}  # type: ignore[typeddict-item]
    if "vehicles" in data:
        import aws_sdk_iotfleetwise.types.update_vehicle_response_items

        out["vehicles"] = (
            aws_sdk_iotfleetwise.types.update_vehicle_response_items.deserialize_aws_json_1_0(
                data["vehicles"]
            )
        )
    if "errors" in data:
        import aws_sdk_iotfleetwise.types.update_vehicle_errors

        out["errors"] = (
            aws_sdk_iotfleetwise.types.update_vehicle_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
