"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialGradientStepColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_gradient_step_color

GeospatialGradientStepColorList: TypeAlias = list[
    "capo_quicksight.types.geospatial_gradient_step_color.GeospatialGradientStepColor"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialGradientStepColorList) -> list:
    import capo_quicksight.types.geospatial_gradient_step_color

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.geospatial_gradient_step_color.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GeospatialGradientStepColorList:
    import capo_quicksight.types.geospatial_gradient_step_color

    out: GeospatialGradientStepColorList = []
    for item in data:
        out.append(
            capo_quicksight.types.geospatial_gradient_step_color.deserialize_json(item)
        )
    return out
