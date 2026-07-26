"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisTickLabelOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.label_options


class AxisTickLabelOptions(TypedDict, closed=True):
    label_options: NotRequired["capo_quicksight.types.label_options.LabelOptions"]
    """<p>Determines whether or not the axis ticks are visible.</p>"""
    rotation_angle: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The rotation angle of the axis tick labels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisTickLabelOptions) -> dict:
    out: dict = {}
    if "label_options" in value:
        import capo_quicksight.types.label_options

        out["LabelOptions"] = capo_quicksight.types.label_options.serialize_json(
            value["label_options"]
        )
    if "rotation_angle" in value:
        out["RotationAngle"] = value["rotation_angle"]
    return out


def deserialize_json(data: dict) -> AxisTickLabelOptions:
    out: AxisTickLabelOptions = {}  # type: ignore[typeddict-item]
    if "LabelOptions" in data:
        import capo_quicksight.types.label_options

        out["label_options"] = capo_quicksight.types.label_options.deserialize_json(
            data["LabelOptions"]
        )
    if "RotationAngle" in data:
        out["rotation_angle"] = data["RotationAngle"]
    return out
