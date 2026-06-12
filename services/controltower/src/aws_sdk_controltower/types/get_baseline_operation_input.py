"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineOperationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.operation_identifier


class GetBaselineOperationInput(TypedDict):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineOperationInput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> GetBaselineOperationInput:
    out: GetBaselineOperationInput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "GetBaselineOperationInput.operation_identifier required"
        )
    return out
