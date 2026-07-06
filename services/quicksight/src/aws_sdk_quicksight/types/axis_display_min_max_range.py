"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisDisplayMinMaxRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double


class AxisDisplayMinMaxRange(TypedDict, closed=True):
    minimum: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The minimum setup for an axis display range.</p>"""
    maximum: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The maximum setup for an axis display range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisDisplayMinMaxRange) -> dict:
    out: dict = {}
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> AxisDisplayMinMaxRange:
    out: AxisDisplayMinMaxRange = {}  # type: ignore[typeddict-item]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    return out
