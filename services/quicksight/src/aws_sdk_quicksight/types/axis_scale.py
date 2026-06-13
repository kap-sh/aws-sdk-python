"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisScale``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_linear_scale
    import aws_sdk_quicksight.types.axis_logarithmic_scale


class AxisScale(TypedDict):
    linear: NotRequired["aws_sdk_quicksight.types.axis_linear_scale.AxisLinearScale"]
    """<p>The linear axis scale setup.</p>"""
    logarithmic: NotRequired[
        "aws_sdk_quicksight.types.axis_logarithmic_scale.AxisLogarithmicScale"
    ]
    """<p>The logarithmic axis scale setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisScale) -> dict:
    out: dict = {}
    if "linear" in value:
        import aws_sdk_quicksight.types.axis_linear_scale

        out["Linear"] = aws_sdk_quicksight.types.axis_linear_scale.serialize_json(
            value["linear"]
        )
    if "logarithmic" in value:
        import aws_sdk_quicksight.types.axis_logarithmic_scale

        out["Logarithmic"] = (
            aws_sdk_quicksight.types.axis_logarithmic_scale.serialize_json(
                value["logarithmic"]
            )
        )
    return out


def deserialize_json(data: dict) -> AxisScale:
    out: AxisScale = {}  # type: ignore[typeddict-item]
    if "Linear" in data:
        import aws_sdk_quicksight.types.axis_linear_scale

        out["linear"] = aws_sdk_quicksight.types.axis_linear_scale.deserialize_json(
            data["Linear"]
        )
    if "Logarithmic" in data:
        import aws_sdk_quicksight.types.axis_logarithmic_scale

        out["logarithmic"] = (
            aws_sdk_quicksight.types.axis_logarithmic_scale.deserialize_json(
                data["Logarithmic"]
            )
        )
    return out
