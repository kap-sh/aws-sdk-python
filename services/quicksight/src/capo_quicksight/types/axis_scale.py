"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisScale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_linear_scale
    import capo_quicksight.types.axis_logarithmic_scale


class AxisScale(TypedDict, closed=True):
    linear: NotRequired["capo_quicksight.types.axis_linear_scale.AxisLinearScale"]
    """<p>The linear axis scale setup.</p>"""
    logarithmic: NotRequired[
        "capo_quicksight.types.axis_logarithmic_scale.AxisLogarithmicScale"
    ]
    """<p>The logarithmic axis scale setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisScale) -> dict:
    out: dict = {}
    if "linear" in value:
        import capo_quicksight.types.axis_linear_scale

        out["Linear"] = capo_quicksight.types.axis_linear_scale.serialize_json(
            value["linear"]
        )
    if "logarithmic" in value:
        import capo_quicksight.types.axis_logarithmic_scale

        out["Logarithmic"] = (
            capo_quicksight.types.axis_logarithmic_scale.serialize_json(
                value["logarithmic"]
            )
        )
    return out


def deserialize_json(data: dict) -> AxisScale:
    out: AxisScale = {}  # type: ignore[typeddict-item]
    if "Linear" in data:
        import capo_quicksight.types.axis_linear_scale

        out["linear"] = capo_quicksight.types.axis_linear_scale.deserialize_json(
            data["Linear"]
        )
    if "Logarithmic" in data:
        import capo_quicksight.types.axis_logarithmic_scale

        out["logarithmic"] = (
            capo_quicksight.types.axis_logarithmic_scale.deserialize_json(
                data["Logarithmic"]
            )
        )
    return out
