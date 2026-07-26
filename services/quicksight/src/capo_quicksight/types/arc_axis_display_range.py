"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcAxisDisplayRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double


class ArcAxisDisplayRange(TypedDict, closed=True):
    min: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The minimum value of the arc axis range.</p>"""
    max: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The maximum value of the arc axis range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArcAxisDisplayRange) -> dict:
    out: dict = {}
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    return out


def deserialize_json(data: dict) -> ArcAxisDisplayRange:
    out: ArcAxisDisplayRange = {}  # type: ignore[typeddict-item]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    return out
