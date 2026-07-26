"""Generated from Smithy shape ``com.amazonaws.controltower#GetControlOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.control_operation


class GetControlOperationOutput(TypedDict, closed=True):
    control_operation: "capo_controltower.types.control_operation.ControlOperation"
    """<p>An operation performed by the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlOperationOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.control_operation

    out["controlOperation"] = capo_controltower.types.control_operation.serialize_json(
        value["control_operation"]
    )
    return out


def deserialize_json(data: dict) -> GetControlOperationOutput:
    out: GetControlOperationOutput = {}  # type: ignore[typeddict-item]
    if "controlOperation" in data:
        import capo_controltower.types.control_operation

        out["control_operation"] = (
            capo_controltower.types.control_operation.deserialize_json(
                data["controlOperation"]
            )
        )
    else:
        raise DeserializationError(
            "GetControlOperationOutput.control_operation required"
        )
    return out
