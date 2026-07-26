"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.string


class WaterfallChartOptions(TypedDict, closed=True):
    total_bar_label: NotRequired["capo_quicksight.types.string.String"]
    """<p>This option determines the total bar label of a waterfall visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartOptions) -> dict:
    out: dict = {}
    if "total_bar_label" in value:
        out["TotalBarLabel"] = value["total_bar_label"]
    return out


def deserialize_json(data: dict) -> WaterfallChartOptions:
    out: WaterfallChartOptions = {}  # type: ignore[typeddict-item]
    if "TotalBarLabel" in data:
        out["total_bar_label"] = data["TotalBarLabel"]
    return out
