"""Generated from Smithy shape ``com.amazonaws.quicksight#DonutOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arc_options
    import aws_sdk_quicksight.types.donut_center_options


class DonutOptions(TypedDict):
    arc_options: NotRequired["aws_sdk_quicksight.types.arc_options.ArcOptions"]
    """<p>The option for define the arc of the chart shape. Valid values are as follows:</p> <ul> <li> <p> <code>WHOLE</code> - A pie chart</p> </li> <li> <p> <code>SMALL</code>- A small-sized donut chart</p> </li> <li> <p> <code>MEDIUM</code>- A medium-sized donut chart</p> </li> <li> <p> <code>LARGE</code>- A large-sized donut chart</p> </li> </ul>"""
    donut_center_options: NotRequired[
        "aws_sdk_quicksight.types.donut_center_options.DonutCenterOptions"
    ]
    """<p>The label options of the label that is displayed in the center of a donut chart. This option isn't available for pie charts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DonutOptions) -> dict:
    out: dict = {}
    if "arc_options" in value:
        import aws_sdk_quicksight.types.arc_options

        out["ArcOptions"] = aws_sdk_quicksight.types.arc_options.serialize_json(
            value["arc_options"]
        )
    if "donut_center_options" in value:
        import aws_sdk_quicksight.types.donut_center_options

        out["DonutCenterOptions"] = (
            aws_sdk_quicksight.types.donut_center_options.serialize_json(
                value["donut_center_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DonutOptions:
    out: DonutOptions = {}  # type: ignore[typeddict-item]
    if "ArcOptions" in data:
        import aws_sdk_quicksight.types.arc_options

        out["arc_options"] = aws_sdk_quicksight.types.arc_options.deserialize_json(
            data["ArcOptions"]
        )
    if "DonutCenterOptions" in data:
        import aws_sdk_quicksight.types.donut_center_options

        out["donut_center_options"] = (
            aws_sdk_quicksight.types.donut_center_options.deserialize_json(
                data["DonutCenterOptions"]
            )
        )
    return out
