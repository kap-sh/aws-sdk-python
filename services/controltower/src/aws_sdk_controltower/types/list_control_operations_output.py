"""Generated from Smithy shape ``com.amazonaws.controltower#ListControlOperationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.control_operations
    import aws_sdk_controltower.types.list_control_operations_next_token


class ListControlOperationsOutput(TypedDict):
    control_operations: (
        "aws_sdk_controltower.types.control_operations.ControlOperations"
    )
    """<p>Returns a list of output from control operations. </p>"""
    next_token: NotRequired[
        "aws_sdk_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
    ]
    """<p>A pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlOperationsOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.control_operations

    out["controlOperations"] = (
        aws_sdk_controltower.types.control_operations.serialize_json(
            value["control_operations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlOperationsOutput:
    out: ListControlOperationsOutput = {}  # type: ignore[typeddict-item]
    if "controlOperations" in data:
        import aws_sdk_controltower.types.control_operations

        out["control_operations"] = (
            aws_sdk_controltower.types.control_operations.deserialize_json(
                data["controlOperations"]
            )
        )
    else:
        raise DeserializationError(
            "ListControlOperationsOutput.control_operations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
