"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialGradientColor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_gradient_step_color_list
    import aws_sdk_quicksight.types.geospatial_null_data_settings
    import aws_sdk_quicksight.types.opacity
    import aws_sdk_quicksight.types.visibility


class GeospatialGradientColor(TypedDict):
    step_colors: "aws_sdk_quicksight.types.geospatial_gradient_step_color_list.GeospatialGradientStepColorList"
    """<p>A list of gradient step colors for the gradient.</p>"""
    null_data_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The state of visibility for null data.</p>"""
    null_data_settings: NotRequired[
        "aws_sdk_quicksight.types.geospatial_null_data_settings.GeospatialNullDataSettings"
    ]
    """<p>The null data visualization settings.</p>"""
    default_opacity: NotRequired["aws_sdk_quicksight.types.opacity.Opacity"]
    """<p>The default opacity for the gradient color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialGradientColor) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.geospatial_gradient_step_color_list

    out["StepColors"] = (
        aws_sdk_quicksight.types.geospatial_gradient_step_color_list.serialize_json(
            value["step_colors"]
        )
    )
    if "null_data_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["NullDataVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["null_data_visibility"]
        )
    if "null_data_settings" in value:
        import aws_sdk_quicksight.types.geospatial_null_data_settings

        out["NullDataSettings"] = (
            aws_sdk_quicksight.types.geospatial_null_data_settings.serialize_json(
                value["null_data_settings"]
            )
        )
    if "default_opacity" in value:
        out["DefaultOpacity"] = value["default_opacity"]
    return out


def deserialize_json(data: dict) -> GeospatialGradientColor:
    out: GeospatialGradientColor = {}  # type: ignore[typeddict-item]
    if "StepColors" in data:
        import aws_sdk_quicksight.types.geospatial_gradient_step_color_list

        out["step_colors"] = (
            aws_sdk_quicksight.types.geospatial_gradient_step_color_list.deserialize_json(
                data["StepColors"]
            )
        )
    else:
        raise DeserializationError("GeospatialGradientColor.step_colors required")
    if "NullDataVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["null_data_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["NullDataVisibility"]
            )
        )
    if "NullDataSettings" in data:
        import aws_sdk_quicksight.types.geospatial_null_data_settings

        out["null_data_settings"] = (
            aws_sdk_quicksight.types.geospatial_null_data_settings.deserialize_json(
                data["NullDataSettings"]
            )
        )
    if "DefaultOpacity" in data:
        out["default_opacity"] = data["DefaultOpacity"]
    return out
