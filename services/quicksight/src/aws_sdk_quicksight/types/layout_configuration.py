"""Generated from Smithy shape ``com.amazonaws.quicksight#LayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.free_form_layout_configuration
    import aws_sdk_quicksight.types.grid_layout_configuration
    import aws_sdk_quicksight.types.section_based_layout_configuration


class LayoutConfiguration(TypedDict, closed=True):
    grid_layout: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_configuration.GridLayoutConfiguration"
    ]
    """<p>A type of layout that can be used on a sheet. In a grid layout, visuals snap to a grid with standard spacing and alignment. Dashboards are displayed as designed, with options to fit to screen or view at actual size. A grid layout can be configured to behave in one of two ways when the viewport is resized: <code>FIXED</code> or <code>RESPONSIVE</code>.</p>"""
    free_form_layout: NotRequired[
        "aws_sdk_quicksight.types.free_form_layout_configuration.FreeFormLayoutConfiguration"
    ]
    """<p>A free-form is optimized for a fixed width and has more control over the exact placement of layout elements.</p>"""
    section_based_layout: NotRequired[
        "aws_sdk_quicksight.types.section_based_layout_configuration.SectionBasedLayoutConfiguration"
    ]
    """<p>A section based layout organizes visuals into multiple sections and has customized header, footer and page break.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutConfiguration) -> dict:
    out: dict = {}
    if "grid_layout" in value:
        import aws_sdk_quicksight.types.grid_layout_configuration

        out["GridLayout"] = (
            aws_sdk_quicksight.types.grid_layout_configuration.serialize_json(
                value["grid_layout"]
            )
        )
    if "free_form_layout" in value:
        import aws_sdk_quicksight.types.free_form_layout_configuration

        out["FreeFormLayout"] = (
            aws_sdk_quicksight.types.free_form_layout_configuration.serialize_json(
                value["free_form_layout"]
            )
        )
    if "section_based_layout" in value:
        import aws_sdk_quicksight.types.section_based_layout_configuration

        out["SectionBasedLayout"] = (
            aws_sdk_quicksight.types.section_based_layout_configuration.serialize_json(
                value["section_based_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> LayoutConfiguration:
    out: LayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "GridLayout" in data:
        import aws_sdk_quicksight.types.grid_layout_configuration

        out["grid_layout"] = (
            aws_sdk_quicksight.types.grid_layout_configuration.deserialize_json(
                data["GridLayout"]
            )
        )
    if "FreeFormLayout" in data:
        import aws_sdk_quicksight.types.free_form_layout_configuration

        out["free_form_layout"] = (
            aws_sdk_quicksight.types.free_form_layout_configuration.deserialize_json(
                data["FreeFormLayout"]
            )
        )
    if "SectionBasedLayout" in data:
        import aws_sdk_quicksight.types.section_based_layout_configuration

        out["section_based_layout"] = (
            aws_sdk_quicksight.types.section_based_layout_configuration.deserialize_json(
                data["SectionBasedLayout"]
            )
        )
    return out
