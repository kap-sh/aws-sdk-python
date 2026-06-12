"""Generated from Smithy shape ``com.amazonaws.controltower#EnableBaselineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.operation_identifier


class EnableBaselineOutput(TypedDict):
    operation_identifier: (
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID (in UUID format) of the asynchronous <code>EnableBaseline</code> operation. This <code>operationIdentifier</code> is used to track status through calls to the <code>GetBaselineOperation</code> API.</p>"""
    arn: "aws_sdk_controltower.types.arn.Arn"
    """<p>The ARN of the <code>EnabledBaseline</code> resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableBaselineOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EnableBaselineOutput:
    out: EnableBaselineOutput = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        raise DeserializationError("EnableBaselineOutput.operation_identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnableBaselineOutput.arn required")
    return out
