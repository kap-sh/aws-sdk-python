"""Generated from Smithy shape ``com.amazonaws.iotwireless#Accuracy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.horizontal_accuracy
    import capo_iot_wireless.types.vertical_accuracy


class Accuracy(TypedDict, closed=True):
    horizontal_accuracy: NotRequired[
        "capo_iot_wireless.types.horizontal_accuracy.HorizontalAccuracy"
    ]
    """<p>The horizontal accuracy of the estimated position, which is the difference between the estimated location and the actual device location.</p>"""
    vertical_accuracy: NotRequired[
        "capo_iot_wireless.types.vertical_accuracy.VerticalAccuracy"
    ]
    """<p>The vertical accuracy of the estimated position, which is the difference between the estimated altitude and actual device latitude in meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Accuracy) -> dict:
    out: dict = {}
    if "horizontal_accuracy" in value:
        out["HorizontalAccuracy"] = value["horizontal_accuracy"]
    if "vertical_accuracy" in value:
        out["VerticalAccuracy"] = value["vertical_accuracy"]
    return out


def deserialize_json(data: dict) -> Accuracy:
    out: Accuracy = {}  # type: ignore[typeddict-item]
    if "HorizontalAccuracy" in data:
        out["horizontal_accuracy"] = data["HorizontalAccuracy"]
    if "VerticalAccuracy" in data:
        out["vertical_accuracy"] = data["VerticalAccuracy"]
    return out
