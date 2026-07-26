"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arc_thickness


class ArcOptions(TypedDict, closed=True):
    arc_thickness: NotRequired["capo_quicksight.types.arc_thickness.ArcThickness"]
    """<p>The arc thickness of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArcOptions) -> dict:
    out: dict = {}
    if "arc_thickness" in value:
        import capo_quicksight.types.arc_thickness

        out["ArcThickness"] = capo_quicksight.types.arc_thickness.serialize_json(
            value["arc_thickness"]
        )
    return out


def deserialize_json(data: dict) -> ArcOptions:
    out: ArcOptions = {}  # type: ignore[typeddict-item]
    if "ArcThickness" in data:
        import capo_quicksight.types.arc_thickness

        out["arc_thickness"] = capo_quicksight.types.arc_thickness.deserialize_json(
            data["ArcThickness"]
        )
    return out
