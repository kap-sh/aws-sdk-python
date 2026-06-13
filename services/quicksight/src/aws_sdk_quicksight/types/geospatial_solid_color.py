"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialSolidColor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_color_state
    import aws_sdk_quicksight.types.hex_color_with_transparency


class GeospatialSolidColor(TypedDict):
    color: (
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    )
    """<p>The color and opacity values for the color.</p>"""
    state: NotRequired[
        "aws_sdk_quicksight.types.geospatial_color_state.GeospatialColorState"
    ]
    """<p>Enables and disables the view state of the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialSolidColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    if "state" in value:
        import aws_sdk_quicksight.types.geospatial_color_state

        out["State"] = aws_sdk_quicksight.types.geospatial_color_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialSolidColor:
    out: GeospatialSolidColor = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("GeospatialSolidColor.color required")
    if "State" in data:
        import aws_sdk_quicksight.types.geospatial_color_state

        out["state"] = aws_sdk_quicksight.types.geospatial_color_state.deserialize_json(
            data["State"]
        )
    return out
