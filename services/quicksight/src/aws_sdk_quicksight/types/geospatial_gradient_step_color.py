"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialGradientStepColor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.hex_color_with_transparency


class GeospatialGradientStepColor(TypedDict, closed=True):
    color: (
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    )
    """<p>The color and opacity values for the gradient step color.</p>"""
    data_value: "aws_sdk_quicksight.types.double.Double"
    """<p>The data value for the gradient step color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialGradientStepColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    out["DataValue"] = value.get("data_value", 0)
    return out


def deserialize_json(data: dict) -> GeospatialGradientStepColor:
    out: GeospatialGradientStepColor = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("GeospatialGradientStepColor.color required")
    if "DataValue" in data:
        out["data_value"] = data["DataValue"]
    else:
        out["data_value"] = 0
    return out
