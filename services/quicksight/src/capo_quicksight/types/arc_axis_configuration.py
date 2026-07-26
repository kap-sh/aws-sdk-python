"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcAxisConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arc_axis_display_range
    import capo_quicksight.types.integer


class ArcAxisConfiguration(TypedDict, closed=True):
    range: NotRequired[
        "capo_quicksight.types.arc_axis_display_range.ArcAxisDisplayRange"
    ]
    """<p>The arc axis range of a <code>GaugeChartVisual</code>.</p>"""
    reserve_range: "capo_quicksight.types.integer.Integer"
    """<p>The reserved range of the arc axis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArcAxisConfiguration) -> dict:
    out: dict = {}
    if "range" in value:
        import capo_quicksight.types.arc_axis_display_range

        out["Range"] = capo_quicksight.types.arc_axis_display_range.serialize_json(
            value["range"]
        )
    out["ReserveRange"] = value.get("reserve_range", 0)
    return out


def deserialize_json(data: dict) -> ArcAxisConfiguration:
    out: ArcAxisConfiguration = {}  # type: ignore[typeddict-item]
    if "Range" in data:
        import capo_quicksight.types.arc_axis_display_range

        out["range"] = capo_quicksight.types.arc_axis_display_range.deserialize_json(
            data["Range"]
        )
    if "ReserveRange" in data:
        out["reserve_range"] = data["ReserveRange"]
    else:
        out["reserve_range"] = 0
    return out
