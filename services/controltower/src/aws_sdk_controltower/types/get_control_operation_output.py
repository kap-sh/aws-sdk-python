"""Generated from Smithy shape ``com.amazonaws.controltower#GetControlOperationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.control_operation


class GetControlOperationOutput(TypedDict):
    control_operation: "aws_sdk_controltower.types.control_operation.ControlOperation"
    """<p>An operation performed by the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlOperationOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.control_operation

    out["controlOperation"] = (
        aws_sdk_controltower.types.control_operation.serialize_json(
            value["control_operation"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetControlOperationOutput:
    out: GetControlOperationOutput = {}  # type: ignore[typeddict-item]
    if "controlOperation" in data:
        import aws_sdk_controltower.types.control_operation

        out["control_operation"] = (
            aws_sdk_controltower.types.control_operation.deserialize_json(
                data["controlOperation"]
            )
        )
    else:
        raise DeserializationError(
            "GetControlOperationOutput.control_operation required"
        )
    return out
