"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialGradientStepColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_gradient_step_color

GeospatialGradientStepColorList: TypeAlias = list[
    "aws_sdk_quicksight.types.geospatial_gradient_step_color.GeospatialGradientStepColor"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialGradientStepColorList) -> list:
    import aws_sdk_quicksight.types.geospatial_gradient_step_color

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.geospatial_gradient_step_color.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GeospatialGradientStepColorList:
    import aws_sdk_quicksight.types.geospatial_gradient_step_color

    out: GeospatialGradientStepColorList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.geospatial_gradient_step_color.deserialize_json(
                item
            )
        )
    return out
