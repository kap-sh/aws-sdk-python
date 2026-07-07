"""Generated from Smithy shape ``com.amazonaws.controltower#EnableControlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.operation_identifier


class EnableControlOutput(TypedDict, closed=True):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>"""
    arn: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>The ARN of the <code>EnabledControl</code> resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableControlOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EnableControlOutput:
    out: EnableControlOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError("EnableControlOutput.operation_identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
