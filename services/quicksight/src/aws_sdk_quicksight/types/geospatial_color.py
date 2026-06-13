"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialColor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_categorical_color
    import aws_sdk_quicksight.types.geospatial_gradient_color
    import aws_sdk_quicksight.types.geospatial_solid_color


class GeospatialColor(TypedDict):
    solid: NotRequired[
        "aws_sdk_quicksight.types.geospatial_solid_color.GeospatialSolidColor"
    ]
    """<p>The visualization properties for the solid color.</p>"""
    gradient: NotRequired[
        "aws_sdk_quicksight.types.geospatial_gradient_color.GeospatialGradientColor"
    ]
    """<p>The visualization properties for the gradient color.</p>"""
    categorical: NotRequired[
        "aws_sdk_quicksight.types.geospatial_categorical_color.GeospatialCategoricalColor"
    ]
    """<p>The visualization properties for the categorical color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialColor) -> dict:
    out: dict = {}
    if "solid" in value:
        import aws_sdk_quicksight.types.geospatial_solid_color

        out["Solid"] = aws_sdk_quicksight.types.geospatial_solid_color.serialize_json(
            value["solid"]
        )
    if "gradient" in value:
        import aws_sdk_quicksight.types.geospatial_gradient_color

        out["Gradient"] = (
            aws_sdk_quicksight.types.geospatial_gradient_color.serialize_json(
                value["gradient"]
            )
        )
    if "categorical" in value:
        import aws_sdk_quicksight.types.geospatial_categorical_color

        out["Categorical"] = (
            aws_sdk_quicksight.types.geospatial_categorical_color.serialize_json(
                value["categorical"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialColor:
    out: GeospatialColor = {}  # type: ignore[typeddict-item]
    if "Solid" in data:
        import aws_sdk_quicksight.types.geospatial_solid_color

        out["solid"] = aws_sdk_quicksight.types.geospatial_solid_color.deserialize_json(
            data["Solid"]
        )
    if "Gradient" in data:
        import aws_sdk_quicksight.types.geospatial_gradient_color

        out["gradient"] = (
            aws_sdk_quicksight.types.geospatial_gradient_color.deserialize_json(
                data["Gradient"]
            )
        )
    if "Categorical" in data:
        import aws_sdk_quicksight.types.geospatial_categorical_color

        out["categorical"] = (
            aws_sdk_quicksight.types.geospatial_categorical_color.deserialize_json(
                data["Categorical"]
            )
        )
    return out
