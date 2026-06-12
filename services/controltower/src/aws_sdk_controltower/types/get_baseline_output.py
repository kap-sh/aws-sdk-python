"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baseline_arn


class GetBaselineOutput(TypedDict):
    arn: "aws_sdk_controltower.types.baseline_arn.BaselineArn"
    """<p>The baseline ARN.</p>"""
    name: "str"
    """<p>A user-friendly name for the baseline.</p>"""
    description: NotRequired["str"]
    """<p>A description of the baseline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetBaselineOutput:
    out: GetBaselineOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetBaselineOutput.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetBaselineOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    return out
