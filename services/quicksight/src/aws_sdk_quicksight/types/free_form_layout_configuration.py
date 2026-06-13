"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.free_form_layout_canvas_size_options
    import aws_sdk_quicksight.types.free_from_layout_element_list
    import aws_sdk_quicksight.types.sheet_layout_group_list


class FreeFormLayoutConfiguration(TypedDict):
    elements: "aws_sdk_quicksight.types.free_from_layout_element_list.FreeFromLayoutElementList"
    """<p>The elements that are included in a free-form layout.</p>"""
    canvas_size_options: NotRequired[
        "aws_sdk_quicksight.types.free_form_layout_canvas_size_options.FreeFormLayoutCanvasSizeOptions"
    ]
    groups: NotRequired[
        "aws_sdk_quicksight.types.sheet_layout_group_list.SheetLayoutGroupList"
    ]
    """<p>The groups that are included in a free-form layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.free_from_layout_element_list

    out["Elements"] = (
        aws_sdk_quicksight.types.free_from_layout_element_list.serialize_json(
            value["elements"]
        )
    )
    if "canvas_size_options" in value:
        import aws_sdk_quicksight.types.free_form_layout_canvas_size_options

        out["CanvasSizeOptions"] = (
            aws_sdk_quicksight.types.free_form_layout_canvas_size_options.serialize_json(
                value["canvas_size_options"]
            )
        )
    if "groups" in value:
        import aws_sdk_quicksight.types.sheet_layout_group_list

        out["Groups"] = aws_sdk_quicksight.types.sheet_layout_group_list.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> FreeFormLayoutConfiguration:
    out: FreeFormLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "Elements" in data:
        import aws_sdk_quicksight.types.free_from_layout_element_list

        out["elements"] = (
            aws_sdk_quicksight.types.free_from_layout_element_list.deserialize_json(
                data["Elements"]
            )
        )
    else:
        raise DeserializationError("FreeFormLayoutConfiguration.elements required")
    if "CanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.free_form_layout_canvas_size_options

        out["canvas_size_options"] = (
            aws_sdk_quicksight.types.free_form_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    if "Groups" in data:
        import aws_sdk_quicksight.types.sheet_layout_group_list

        out["groups"] = (
            aws_sdk_quicksight.types.sheet_layout_group_list.deserialize_json(
                data["Groups"]
            )
        )
    return out
