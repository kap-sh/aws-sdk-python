"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisDisplayRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_data_driven_range
    import capo_quicksight.types.axis_display_min_max_range


class AxisDisplayRange(TypedDict, closed=True):
    min_max: NotRequired[
        "capo_quicksight.types.axis_display_min_max_range.AxisDisplayMinMaxRange"
    ]
    """<p>The minimum and maximum setup of an axis display range.</p>"""
    data_driven: NotRequired[
        "capo_quicksight.types.axis_display_data_driven_range.AxisDisplayDataDrivenRange"
    ]
    """<p>The data-driven setup of an axis display range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisDisplayRange) -> dict:
    out: dict = {}
    if "min_max" in value:
        import capo_quicksight.types.axis_display_min_max_range

        out["MinMax"] = capo_quicksight.types.axis_display_min_max_range.serialize_json(
            value["min_max"]
        )
    if "data_driven" in value:
        import capo_quicksight.types.axis_display_data_driven_range

        out["DataDriven"] = (
            capo_quicksight.types.axis_display_data_driven_range.serialize_json(
                value["data_driven"]
            )
        )
    return out


def deserialize_json(data: dict) -> AxisDisplayRange:
    out: AxisDisplayRange = {}  # type: ignore[typeddict-item]
    if "MinMax" in data:
        import capo_quicksight.types.axis_display_min_max_range

        out["min_max"] = (
            capo_quicksight.types.axis_display_min_max_range.deserialize_json(
                data["MinMax"]
            )
        )
    if "DataDriven" in data:
        import capo_quicksight.types.axis_display_data_driven_range

        out["data_driven"] = (
            capo_quicksight.types.axis_display_data_driven_range.deserialize_json(
                data["DataDriven"]
            )
        )
    return out
