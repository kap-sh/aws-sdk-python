"""Generated from Smithy shape ``com.amazonaws.controltower#CreateLandingZoneOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.operation_identifier


class CreateLandingZoneOutput(TypedDict):
    arn: "aws_sdk_controltower.types.arn.Arn"
    """<p>The ARN of the landing zone resource.</p>"""
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>A unique identifier assigned to a <code>CreateLandingZone</code> operation. You can use this identifier as an input of <code>GetLandingZoneOperation</code> to check the operation's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLandingZoneOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> CreateLandingZoneOutput:
    out: CreateLandingZoneOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateLandingZoneOutput.arn required")
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "CreateLandingZoneOutput.operation_identifier required"
        )
    return out
