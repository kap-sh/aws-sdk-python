"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baseline_arn


class GetBaselineInput(TypedDict, closed=True):
    baseline_identifier: "aws_sdk_controltower.types.baseline_arn.BaselineArn"
    """<p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineInput) -> dict:
    out: dict = {}
    out["baselineIdentifier"] = value["baseline_identifier"]
    return out


def deserialize_json(data: dict) -> GetBaselineInput:
    out: GetBaselineInput = {}  # type: ignore[typeddict-item]
    if "baselineIdentifier" in data:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        raise DeserializationError("GetBaselineInput.baseline_identifier required")
    return out
