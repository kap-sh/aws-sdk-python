"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#BatchCreateVehicleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.create_vehicle_errors
    import capo_iotfleetwise.types.create_vehicle_responses


class BatchCreateVehicleResponse(TypedDict, closed=True):
    vehicles: NotRequired[
        "capo_iotfleetwise.types.create_vehicle_responses.createVehicleResponses"
    ]
    """<p> A list of information about a batch of created vehicles. For more information, see the API data type.</p>"""
    errors: NotRequired[
        "capo_iotfleetwise.types.create_vehicle_errors.createVehicleErrors"
    ]
    """<p>A list of information about creation errors, or an empty list if there aren't any errors. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateVehicleResponse) -> dict:
    out: dict = {}
    if "vehicles" in value:
        import capo_iotfleetwise.types.create_vehicle_responses

        out["vehicles"] = (
            capo_iotfleetwise.types.create_vehicle_responses.serialize_aws_json_1_0(
                value["vehicles"]
            )
        )
    if "errors" in value:
        import capo_iotfleetwise.types.create_vehicle_errors

        out["errors"] = (
            capo_iotfleetwise.types.create_vehicle_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateVehicleResponse:
    out: BatchCreateVehicleResponse = {}  # type: ignore[typeddict-item]
    if "vehicles" in data:
        import capo_iotfleetwise.types.create_vehicle_responses

        out["vehicles"] = (
            capo_iotfleetwise.types.create_vehicle_responses.deserialize_aws_json_1_0(
                data["vehicles"]
            )
        )
    if "errors" in data:
        import capo_iotfleetwise.types.create_vehicle_errors

        out["errors"] = (
            capo_iotfleetwise.types.create_vehicle_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
