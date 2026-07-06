"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arc_thickness_options
    import aws_sdk_quicksight.types.double


class ArcConfiguration(TypedDict, closed=True):
    arc_angle: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The option that determines the arc angle of a <code>GaugeChartVisual</code>.</p>"""
    arc_thickness: NotRequired[
        "aws_sdk_quicksight.types.arc_thickness_options.ArcThicknessOptions"
    ]
    """<p>The options that determine the arc thickness of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArcConfiguration) -> dict:
    out: dict = {}
    if "arc_angle" in value:
        out["ArcAngle"] = value["arc_angle"]
    if "arc_thickness" in value:
        import aws_sdk_quicksight.types.arc_thickness_options

        out["ArcThickness"] = (
            aws_sdk_quicksight.types.arc_thickness_options.serialize_json(
                value["arc_thickness"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArcConfiguration:
    out: ArcConfiguration = {}  # type: ignore[typeddict-item]
    if "ArcAngle" in data:
        out["arc_angle"] = data["ArcAngle"]
    if "ArcThickness" in data:
        import aws_sdk_quicksight.types.arc_thickness_options

        out["arc_thickness"] = (
            aws_sdk_quicksight.types.arc_thickness_options.deserialize_json(
                data["ArcThickness"]
            )
        )
    return out
