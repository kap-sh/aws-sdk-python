"""Generated from Smithy shape ``com.amazonaws.controltower#ResetEnabledBaselineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.operation_identifier


class ResetEnabledBaselineOutput(TypedDict, closed=True):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID (in UUID format) of the asynchronous <code>ResetEnabledBaseline</code> operation. This <code>operationIdentifier</code> is used to track status through calls to the <code>GetBaselineOperation</code> API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetEnabledBaselineOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> ResetEnabledBaselineOutput:
    out: ResetEnabledBaselineOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError(
            "ResetEnabledBaselineOutput.operation_identifier required"
        )
    return out
