"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_categorical_color
    import capo_quicksight.types.geospatial_gradient_color
    import capo_quicksight.types.geospatial_solid_color


class GeospatialColor(TypedDict, closed=True):
    solid: NotRequired[
        "capo_quicksight.types.geospatial_solid_color.GeospatialSolidColor"
    ]
    """<p>The visualization properties for the solid color.</p>"""
    gradient: NotRequired[
        "capo_quicksight.types.geospatial_gradient_color.GeospatialGradientColor"
    ]
    """<p>The visualization properties for the gradient color.</p>"""
    categorical: NotRequired[
        "capo_quicksight.types.geospatial_categorical_color.GeospatialCategoricalColor"
    ]
    """<p>The visualization properties for the categorical color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialColor) -> dict:
    out: dict = {}
    if "solid" in value:
        import capo_quicksight.types.geospatial_solid_color

        out["Solid"] = capo_quicksight.types.geospatial_solid_color.serialize_json(
            value["solid"]
        )
    if "gradient" in value:
        import capo_quicksight.types.geospatial_gradient_color

        out["Gradient"] = (
            capo_quicksight.types.geospatial_gradient_color.serialize_json(
                value["gradient"]
            )
        )
    if "categorical" in value:
        import capo_quicksight.types.geospatial_categorical_color

        out["Categorical"] = (
            capo_quicksight.types.geospatial_categorical_color.serialize_json(
                value["categorical"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialColor:
    out: GeospatialColor = {}  # type: ignore[typeddict-item]
    if "Solid" in data:
        import capo_quicksight.types.geospatial_solid_color

        out["solid"] = capo_quicksight.types.geospatial_solid_color.deserialize_json(
            data["Solid"]
        )
    if "Gradient" in data:
        import capo_quicksight.types.geospatial_gradient_color

        out["gradient"] = (
            capo_quicksight.types.geospatial_gradient_color.deserialize_json(
                data["Gradient"]
            )
        )
    if "Categorical" in data:
        import capo_quicksight.types.geospatial_categorical_color

        out["categorical"] = (
            capo_quicksight.types.geospatial_categorical_color.deserialize_json(
                data["Categorical"]
            )
        )
    return out
