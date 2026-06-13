"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultInteractiveLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.default_free_form_layout_configuration
    import aws_sdk_quicksight.types.default_grid_layout_configuration


class DefaultInteractiveLayoutConfiguration(TypedDict):
    grid: NotRequired[
        "aws_sdk_quicksight.types.default_grid_layout_configuration.DefaultGridLayoutConfiguration"
    ]
    """<p>The options that determine the default settings for a grid layout configuration.</p>"""
    free_form: NotRequired[
        "aws_sdk_quicksight.types.default_free_form_layout_configuration.DefaultFreeFormLayoutConfiguration"
    ]
    """<p>The options that determine the default settings of a free-form layout configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultInteractiveLayoutConfiguration) -> dict:
    out: dict = {}
    if "grid" in value:
        import aws_sdk_quicksight.types.default_grid_layout_configuration

        out["Grid"] = (
            aws_sdk_quicksight.types.default_grid_layout_configuration.serialize_json(
                value["grid"]
            )
        )
    if "free_form" in value:
        import aws_sdk_quicksight.types.default_free_form_layout_configuration

        out["FreeForm"] = (
            aws_sdk_quicksight.types.default_free_form_layout_configuration.serialize_json(
                value["free_form"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultInteractiveLayoutConfiguration:
    out: DefaultInteractiveLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "Grid" in data:
        import aws_sdk_quicksight.types.default_grid_layout_configuration

        out["grid"] = (
            aws_sdk_quicksight.types.default_grid_layout_configuration.deserialize_json(
                data["Grid"]
            )
        )
    if "FreeForm" in data:
        import aws_sdk_quicksight.types.default_free_form_layout_configuration

        out["free_form"] = (
            aws_sdk_quicksight.types.default_free_form_layout_configuration.deserialize_json(
                data["FreeForm"]
            )
        )
    return out
