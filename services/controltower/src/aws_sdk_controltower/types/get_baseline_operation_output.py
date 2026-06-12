"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineOperationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baseline_operation


class GetBaselineOperationOutput(TypedDict):
    baseline_operation: (
        "aws_sdk_controltower.types.baseline_operation.BaselineOperation"
    )
    """<p>A <code>baselineOperation</code> object that shows information about the specified operation ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineOperationOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.baseline_operation

    out["baselineOperation"] = (
        aws_sdk_controltower.types.baseline_operation.serialize_json(
            value["baseline_operation"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBaselineOperationOutput:
    out: GetBaselineOperationOutput = {}  # type: ignore[typeddict-item]
    if "baselineOperation" in data:
        import aws_sdk_controltower.types.baseline_operation

        out["baseline_operation"] = (
            aws_sdk_controltower.types.baseline_operation.deserialize_json(
                data["baselineOperation"]
            )
        )
    else:
        raise DeserializationError(
            "GetBaselineOperationOutput.baseline_operation required"
        )
    return out
