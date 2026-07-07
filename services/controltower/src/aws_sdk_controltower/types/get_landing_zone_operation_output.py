"""Generated from Smithy shape ``com.amazonaws.controltower#GetLandingZoneOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_operation_detail


class GetLandingZoneOperationOutput(TypedDict, closed=True):
    operation_details: "aws_sdk_controltower.types.landing_zone_operation_detail.LandingZoneOperationDetail"
    """<p>Details about a landing zone operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLandingZoneOperationOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.landing_zone_operation_detail

    out["operationDetails"] = (
        aws_sdk_controltower.types.landing_zone_operation_detail.serialize_json(
            value["operation_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetLandingZoneOperationOutput:
    out: GetLandingZoneOperationOutput = {}  # type: ignore[typeddict-item]
    if "operationDetails" in data:
        import aws_sdk_controltower.types.landing_zone_operation_detail

        out["operation_details"] = (
            aws_sdk_controltower.types.landing_zone_operation_detail.deserialize_json(
                data["operationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetLandingZoneOperationOutput.operation_details required"
        )
    return out
