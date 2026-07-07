"""Generated from Smithy shape ``com.amazonaws.quicksight#RangeConstant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string


class RangeConstant(TypedDict, closed=True):
    minimum: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The minimum value for a range constant.</p>"""
    maximum: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The maximum value for a range constant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangeConstant) -> dict:
    out: dict = {}
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> RangeConstant:
    out: RangeConstant = {}  # type: ignore[typeddict-item]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    return out
