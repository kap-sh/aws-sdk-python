"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.border_radius
    import aws_sdk_quicksight.types.grid_layout_element_background_style
    import aws_sdk_quicksight.types.grid_layout_element_border_style
    import aws_sdk_quicksight.types.grid_layout_element_column_index
    import aws_sdk_quicksight.types.grid_layout_element_column_span
    import aws_sdk_quicksight.types.grid_layout_element_row_index
    import aws_sdk_quicksight.types.grid_layout_element_row_span
    import aws_sdk_quicksight.types.layout_element_type
    import aws_sdk_quicksight.types.loading_animation
    import aws_sdk_quicksight.types.padding
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class GridLayoutElement(TypedDict, closed=True):
    element_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>A unique identifier for an element within a grid layout.</p>"""
    element_type: "aws_sdk_quicksight.types.layout_element_type.LayoutElementType"
    """<p>The type of element.</p>"""
    column_index: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_element_column_index.GridLayoutElementColumnIndex"
    ]
    """<p>The column index for the upper left corner of an element.</p>"""
    column_span: "aws_sdk_quicksight.types.grid_layout_element_column_span.GridLayoutElementColumnSpan"
    """<p>The width of a grid element expressed as a number of grid columns.</p>"""
    row_index: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_element_row_index.GridLayoutElementRowIndex"
    ]
    """<p>The row index for the upper left corner of an element.</p>"""
    row_span: (
        "aws_sdk_quicksight.types.grid_layout_element_row_span.GridLayoutElementRowSpan"
    )
    """<p>The height of a grid element expressed as a number of grid rows.</p>"""
    border_style: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_element_border_style.GridLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a grid layout element.</p>"""
    selected_border_style: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_element_border_style.GridLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a grid layout element. This border style is used when the element is selected.</p>"""
    background_style: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_element_background_style.GridLayoutElementBackgroundStyle"
    ]
    """<p>The background style configuration of a grid layout element.</p>"""
    loading_animation: NotRequired[
        "aws_sdk_quicksight.types.loading_animation.LoadingAnimation"
    ]
    border_radius: NotRequired["aws_sdk_quicksight.types.border_radius.BorderRadius"]
    """<p>The border radius of a grid layout element.</p>"""
    padding: NotRequired["aws_sdk_quicksight.types.padding.Padding"]
    """<p>The padding of a grid layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutElement) -> dict:
    out: dict = {}
    out["ElementId"] = value["element_id"]
    import aws_sdk_quicksight.types.layout_element_type

    out["ElementType"] = aws_sdk_quicksight.types.layout_element_type.serialize_json(
        value["element_type"]
    )
    if "column_index" in value:
        out["ColumnIndex"] = value["column_index"]
    out["ColumnSpan"] = value["column_span"]
    if "row_index" in value:
        out["RowIndex"] = value["row_index"]
    out["RowSpan"] = value["row_span"]
    if "border_style" in value:
        import aws_sdk_quicksight.types.grid_layout_element_border_style

        out["BorderStyle"] = (
            aws_sdk_quicksight.types.grid_layout_element_border_style.serialize_json(
                value["border_style"]
            )
        )
    if "selected_border_style" in value:
        import aws_sdk_quicksight.types.grid_layout_element_border_style

        out["SelectedBorderStyle"] = (
            aws_sdk_quicksight.types.grid_layout_element_border_style.serialize_json(
                value["selected_border_style"]
            )
        )
    if "background_style" in value:
        import aws_sdk_quicksight.types.grid_layout_element_background_style

        out["BackgroundStyle"] = (
            aws_sdk_quicksight.types.grid_layout_element_background_style.serialize_json(
                value["background_style"]
            )
        )
    if "loading_animation" in value:
        import aws_sdk_quicksight.types.loading_animation

        out["LoadingAnimation"] = (
            aws_sdk_quicksight.types.loading_animation.serialize_json(
                value["loading_animation"]
            )
        )
    if "border_radius" in value:
        out["BorderRadius"] = value["border_radius"]
    if "padding" in value:
        out["Padding"] = value["padding"]
    return out


def deserialize_json(data: dict) -> GridLayoutElement:
    out: GridLayoutElement = {}  # type: ignore[typeddict-item]
    if "ElementId" in data:
        out["element_id"] = data["ElementId"]
    else:
        raise DeserializationError("GridLayoutElement.element_id required")
    if "ElementType" in data:
        import aws_sdk_quicksight.types.layout_element_type

        out["element_type"] = (
            aws_sdk_quicksight.types.layout_element_type.deserialize_json(
                data["ElementType"]
            )
        )
    else:
        raise DeserializationError("GridLayoutElement.element_type required")
    if "ColumnIndex" in data:
        out["column_index"] = data["ColumnIndex"]
    if "ColumnSpan" in data:
        out["column_span"] = data["ColumnSpan"]
    else:
        raise DeserializationError("GridLayoutElement.column_span required")
    if "RowIndex" in data:
        out["row_index"] = data["RowIndex"]
    if "RowSpan" in data:
        out["row_span"] = data["RowSpan"]
    else:
        raise DeserializationError("GridLayoutElement.row_span required")
    if "BorderStyle" in data:
        import aws_sdk_quicksight.types.grid_layout_element_border_style

        out["border_style"] = (
            aws_sdk_quicksight.types.grid_layout_element_border_style.deserialize_json(
                data["BorderStyle"]
            )
        )
    if "SelectedBorderStyle" in data:
        import aws_sdk_quicksight.types.grid_layout_element_border_style

        out["selected_border_style"] = (
            aws_sdk_quicksight.types.grid_layout_element_border_style.deserialize_json(
                data["SelectedBorderStyle"]
            )
        )
    if "BackgroundStyle" in data:
        import aws_sdk_quicksight.types.grid_layout_element_background_style

        out["background_style"] = (
            aws_sdk_quicksight.types.grid_layout_element_background_style.deserialize_json(
                data["BackgroundStyle"]
            )
        )
    if "LoadingAnimation" in data:
        import aws_sdk_quicksight.types.loading_animation

        out["loading_animation"] = (
            aws_sdk_quicksight.types.loading_animation.deserialize_json(
                data["LoadingAnimation"]
            )
        )
    if "BorderRadius" in data:
        out["border_radius"] = data["BorderRadius"]
    if "Padding" in data:
        out["padding"] = data["Padding"]
    return out
