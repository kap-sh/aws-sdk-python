"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLinearScale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.integer


class AxisLinearScale(TypedDict, closed=True):
    step_count: NotRequired["aws_sdk_quicksight.types.integer.Integer"]
    """<p>The step count setup of a linear axis.</p>"""
    step_size: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The step size setup of a linear axis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisLinearScale) -> dict:
    out: dict = {}
    if "step_count" in value:
        out["StepCount"] = value["step_count"]
    if "step_size" in value:
        out["StepSize"] = value["step_size"]
    return out


def deserialize_json(data: dict) -> AxisLinearScale:
    out: AxisLinearScale = {}  # type: ignore[typeddict-item]
    if "StepCount" in data:
        out["step_count"] = data["StepCount"]
    if "StepSize" in data:
        out["step_size"] = data["StepSize"]
    return out
