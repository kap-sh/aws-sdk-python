"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultInteractiveLayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.default_free_form_layout_configuration
    import capo_quicksight.types.default_grid_layout_configuration


class DefaultInteractiveLayoutConfiguration(TypedDict, closed=True):
    grid: NotRequired[
        "capo_quicksight.types.default_grid_layout_configuration.DefaultGridLayoutConfiguration"
    ]
    """<p>The options that determine the default settings for a grid layout configuration.</p>"""
    free_form: NotRequired[
        "capo_quicksight.types.default_free_form_layout_configuration.DefaultFreeFormLayoutConfiguration"
    ]
    """<p>The options that determine the default settings of a free-form layout configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultInteractiveLayoutConfiguration) -> dict:
    out: dict = {}
    if "grid" in value:
        import capo_quicksight.types.default_grid_layout_configuration

        out["Grid"] = (
            capo_quicksight.types.default_grid_layout_configuration.serialize_json(
                value["grid"]
            )
        )
    if "free_form" in value:
        import capo_quicksight.types.default_free_form_layout_configuration

        out["FreeForm"] = (
            capo_quicksight.types.default_free_form_layout_configuration.serialize_json(
                value["free_form"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultInteractiveLayoutConfiguration:
    out: DefaultInteractiveLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "Grid" in data:
        import capo_quicksight.types.default_grid_layout_configuration

        out["grid"] = (
            capo_quicksight.types.default_grid_layout_configuration.deserialize_json(
                data["Grid"]
            )
        )
    if "FreeForm" in data:
        import capo_quicksight.types.default_free_form_layout_configuration

        out["free_form"] = (
            capo_quicksight.types.default_free_form_layout_configuration.deserialize_json(
                data["FreeForm"]
            )
        )
    return out
