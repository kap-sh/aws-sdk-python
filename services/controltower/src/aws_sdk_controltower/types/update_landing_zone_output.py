"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateLandingZoneOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.operation_identifier


class UpdateLandingZoneOutput(TypedDict):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>A unique identifier assigned to a <code>UpdateLandingZone</code> operation. You can use this identifier as an input of <code>GetLandingZoneOperation</code> to check the operation's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLandingZoneOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateLandingZoneOutput:
    out: UpdateLandingZoneOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "UpdateLandingZoneOutput.operation_identifier required"
        )
    return out
