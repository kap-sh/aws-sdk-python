"""Generated from Smithy shape ``com.amazonaws.controltower#DisableControlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.operation_identifier


class DisableControlOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableControlOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> DisableControlOutput:
    out: DisableControlOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError("DisableControlOutput.operation_identifier required")
    return out
