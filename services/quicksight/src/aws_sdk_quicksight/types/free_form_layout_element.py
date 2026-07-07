"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.border_radius
    import aws_sdk_quicksight.types.free_form_layout_element_background_style
    import aws_sdk_quicksight.types.free_form_layout_element_border_style
    import aws_sdk_quicksight.types.layout_element_type
    import aws_sdk_quicksight.types.loading_animation
    import aws_sdk_quicksight.types.padding
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.sheet_element_rendering_rule_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.unlimited_pixel_length
    import aws_sdk_quicksight.types.visibility


class FreeFormLayoutElement(TypedDict, closed=True):
    element_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>A unique identifier for an element within a free-form layout.</p>"""
    element_type: "aws_sdk_quicksight.types.layout_element_type.LayoutElementType"
    """<p>The type of element.</p>"""
    x_axis_location: "aws_sdk_quicksight.types.pixel_length.PixelLength"
    """<p>The x-axis coordinate of the element.</p>"""
    y_axis_location: (
        "aws_sdk_quicksight.types.unlimited_pixel_length.UnlimitedPixelLength"
    )
    """<p>The y-axis coordinate of the element.</p>"""
    width: "aws_sdk_quicksight.types.pixel_length.PixelLength"
    """<p>The width of an element within a free-form layout.</p>"""
    height: "aws_sdk_quicksight.types.pixel_length.PixelLength"
    """<p>The height of an element within a free-form layout.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of an element within a free-form layout.</p>"""
    rendering_rules: NotRequired[
        "aws_sdk_quicksight.types.sheet_element_rendering_rule_list.SheetElementRenderingRuleList"
    ]
    """<p>The rendering rules that determine when an element should be displayed within a free-form layout.</p>"""
    border_style: NotRequired[
        "aws_sdk_quicksight.types.free_form_layout_element_border_style.FreeFormLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a free-form layout element.</p>"""
    selected_border_style: NotRequired[
        "aws_sdk_quicksight.types.free_form_layout_element_border_style.FreeFormLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a free-form layout element. This border style is used when the element is selected.</p>"""
    background_style: NotRequired[
        "aws_sdk_quicksight.types.free_form_layout_element_background_style.FreeFormLayoutElementBackgroundStyle"
    ]
    """<p>The background style configuration of a free-form layout element.</p>"""
    loading_animation: NotRequired[
        "aws_sdk_quicksight.types.loading_animation.LoadingAnimation"
    ]
    """<p>The loading animation configuration of a free-form layout element.</p>"""
    border_radius: NotRequired["aws_sdk_quicksight.types.border_radius.BorderRadius"]
    """<p>The border radius of a free-form layout element.</p>"""
    padding: NotRequired["aws_sdk_quicksight.types.padding.Padding"]
    """<p>The padding of a free-form layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutElement) -> dict:
    out: dict = {}
    out["ElementId"] = value["element_id"]
    import aws_sdk_quicksight.types.layout_element_type

    out["ElementType"] = aws_sdk_quicksight.types.layout_element_type.serialize_json(
        value["element_type"]
    )
    out["XAxisLocation"] = value["x_axis_location"]
    out["YAxisLocation"] = value["y_axis_location"]
    out["Width"] = value["width"]
    out["Height"] = value["height"]
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "rendering_rules" in value:
        import aws_sdk_quicksight.types.sheet_element_rendering_rule_list

        out["RenderingRules"] = (
            aws_sdk_quicksight.types.sheet_element_rendering_rule_list.serialize_json(
                value["rendering_rules"]
            )
        )
    if "border_style" in value:
        import aws_sdk_quicksight.types.free_form_layout_element_border_style

        out["BorderStyle"] = (
            aws_sdk_quicksight.types.free_form_layout_element_border_style.serialize_json(
                value["border_style"]
            )
        )
    if "selected_border_style" in value:
        import aws_sdk_quicksight.types.free_form_layout_element_border_style

        out["SelectedBorderStyle"] = (
            aws_sdk_quicksight.types.free_form_layout_element_border_style.serialize_json(
                value["selected_border_style"]
            )
        )
    if "background_style" in value:
        import aws_sdk_quicksight.types.free_form_layout_element_background_style

        out["BackgroundStyle"] = (
            aws_sdk_quicksight.types.free_form_layout_element_background_style.serialize_json(
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


def deserialize_json(data: dict) -> FreeFormLayoutElement:
    out: FreeFormLayoutElement = {}  # type: ignore[typeddict-item]
    if "ElementId" in data:
        out["element_id"] = data["ElementId"]
    else:
        raise DeserializationError("FreeFormLayoutElement.element_id required")
    if "ElementType" in data:
        import aws_sdk_quicksight.types.layout_element_type

        out["element_type"] = (
            aws_sdk_quicksight.types.layout_element_type.deserialize_json(
                data["ElementType"]
            )
        )
    else:
        raise DeserializationError("FreeFormLayoutElement.element_type required")
    if "XAxisLocation" in data:
        out["x_axis_location"] = data["XAxisLocation"]
    else:
        raise DeserializationError("FreeFormLayoutElement.x_axis_location required")
    if "YAxisLocation" in data:
        out["y_axis_location"] = data["YAxisLocation"]
    else:
        raise DeserializationError("FreeFormLayoutElement.y_axis_location required")
    if "Width" in data:
        out["width"] = data["Width"]
    else:
        raise DeserializationError("FreeFormLayoutElement.width required")
    if "Height" in data:
        out["height"] = data["Height"]
    else:
        raise DeserializationError("FreeFormLayoutElement.height required")
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "RenderingRules" in data:
        import aws_sdk_quicksight.types.sheet_element_rendering_rule_list

        out["rendering_rules"] = (
            aws_sdk_quicksight.types.sheet_element_rendering_rule_list.deserialize_json(
                data["RenderingRules"]
            )
        )
    if "BorderStyle" in data:
        import aws_sdk_quicksight.types.free_form_layout_element_border_style

        out["border_style"] = (
            aws_sdk_quicksight.types.free_form_layout_element_border_style.deserialize_json(
                data["BorderStyle"]
            )
        )
    if "SelectedBorderStyle" in data:
        import aws_sdk_quicksight.types.free_form_layout_element_border_style

        out["selected_border_style"] = (
            aws_sdk_quicksight.types.free_form_layout_element_border_style.deserialize_json(
                data["SelectedBorderStyle"]
            )
        )
    if "BackgroundStyle" in data:
        import aws_sdk_quicksight.types.free_form_layout_element_background_style

        out["background_style"] = (
            aws_sdk_quicksight.types.free_form_layout_element_background_style.deserialize_json(
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
