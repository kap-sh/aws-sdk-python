"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledControlOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.operation_identifier


class UpdateEnabledControlOutput(TypedDict):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p> The operation identifier for this <code>UpdateEnabledControl</code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledControlOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledControlOutput:
    out: UpdateEnabledControlOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "UpdateEnabledControlOutput.operation_identifier required"
        )
    return out
