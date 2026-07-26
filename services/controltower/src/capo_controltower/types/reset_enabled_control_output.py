"""Generated from Smithy shape ``com.amazonaws.controltower#ResetEnabledControlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.operation_identifier


class ResetEnabledControlOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p> The operation identifier for this <code>ResetEnabledControl</code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetEnabledControlOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> ResetEnabledControlOutput:
    out: ResetEnabledControlOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "ResetEnabledControlOutput.operation_identifier required"
        )
    return out
