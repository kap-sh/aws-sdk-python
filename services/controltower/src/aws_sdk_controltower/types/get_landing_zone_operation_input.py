"""Generated from Smithy shape ``com.amazonaws.controltower#GetLandingZoneOperationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.operation_identifier


class GetLandingZoneOperationInput(TypedDict):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>A unique identifier assigned to a landing zone operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLandingZoneOperationInput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> GetLandingZoneOperationInput:
    out: GetLandingZoneOperationInput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "GetLandingZoneOperationInput.operation_identifier required"
        )
    return out
