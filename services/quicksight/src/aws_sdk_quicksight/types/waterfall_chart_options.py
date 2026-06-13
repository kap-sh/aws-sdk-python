"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class WaterfallChartOptions(TypedDict):
    total_bar_label: NotRequired["aws_sdk_quicksight.types.string.String"]
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
