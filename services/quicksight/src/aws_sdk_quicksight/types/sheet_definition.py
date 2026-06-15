"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_control_list
    import aws_sdk_quicksight.types.layout_list
    import aws_sdk_quicksight.types.parameter_control_list
    import aws_sdk_quicksight.types.sheet_content_type
    import aws_sdk_quicksight.types.sheet_control_layout_list
    import aws_sdk_quicksight.types.sheet_description
    import aws_sdk_quicksight.types.sheet_image_list
    import aws_sdk_quicksight.types.sheet_name
    import aws_sdk_quicksight.types.sheet_text_box_list
    import aws_sdk_quicksight.types.sheet_title
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.visual_custom_action_defaults
    import aws_sdk_quicksight.types.visual_list


class SheetDefinition(TypedDict):
    sheet_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of a sheet.</p>"""
    title: NotRequired["aws_sdk_quicksight.types.sheet_title.SheetTitle"]
    """<p>The title of the sheet.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.sheet_description.SheetDescription"
    ]
    """<p>A description of the sheet.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.sheet_name.SheetName"]
    """<p>The name of the sheet. This name is displayed on the sheet's tab in the Quick console.</p>"""
    parameter_controls: NotRequired[
        "aws_sdk_quicksight.types.parameter_control_list.ParameterControlList"
    ]
    r"""<p>The list of parameter controls that are on a sheet.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html\">Using a Control with a Parameter in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    filter_controls: NotRequired[
        "aws_sdk_quicksight.types.filter_control_list.FilterControlList"
    ]
    r"""<p>The list of filter controls that are on a sheet.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html\">Adding filter controls to analysis sheets</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    visuals: NotRequired["aws_sdk_quicksight.types.visual_list.VisualList"]
    """<p>A list of the visuals that are on a sheet. Visual placement is determined by the layout of the sheet.</p>"""
    text_boxes: NotRequired[
        "aws_sdk_quicksight.types.sheet_text_box_list.SheetTextBoxList"
    ]
    """<p>The text boxes that are on a sheet.</p>"""
    images: NotRequired["aws_sdk_quicksight.types.sheet_image_list.SheetImageList"]
    """<p>A list of images on a sheet.</p>"""
    layouts: NotRequired["aws_sdk_quicksight.types.layout_list.LayoutList"]
    r"""<p>Layouts define how the components of a sheet are arranged.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html\">Types of layout</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    sheet_control_layouts: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_layout_list.SheetControlLayoutList"
    ]
    """<p>The control layouts of the sheet.</p>"""
    content_type: NotRequired[
        "aws_sdk_quicksight.types.sheet_content_type.SheetContentType"
    ]
    """<p>The layout content type of the sheet. Choose one of the following options:</p> <ul> <li> <p> <code>PAGINATED</code>: Creates a sheet for a paginated report.</p> </li> <li> <p> <code>INTERACTIVE</code>: Creates a sheet for an interactive dashboard.</p> </li> </ul>"""
    custom_action_defaults: NotRequired[
        "aws_sdk_quicksight.types.visual_custom_action_defaults.VisualCustomActionDefaults"
    ]
    """<p>A list of visual custom actions for the sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetDefinition) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "parameter_controls" in value:
        import aws_sdk_quicksight.types.parameter_control_list

        out["ParameterControls"] = (
            aws_sdk_quicksight.types.parameter_control_list.serialize_json(
                value["parameter_controls"]
            )
        )
    if "filter_controls" in value:
        import aws_sdk_quicksight.types.filter_control_list

        out["FilterControls"] = (
            aws_sdk_quicksight.types.filter_control_list.serialize_json(
                value["filter_controls"]
            )
        )
    if "visuals" in value:
        import aws_sdk_quicksight.types.visual_list

        out["Visuals"] = aws_sdk_quicksight.types.visual_list.serialize_json(
            value["visuals"]
        )
    if "text_boxes" in value:
        import aws_sdk_quicksight.types.sheet_text_box_list

        out["TextBoxes"] = aws_sdk_quicksight.types.sheet_text_box_list.serialize_json(
            value["text_boxes"]
        )
    if "images" in value:
        import aws_sdk_quicksight.types.sheet_image_list

        out["Images"] = aws_sdk_quicksight.types.sheet_image_list.serialize_json(
            value["images"]
        )
    if "layouts" in value:
        import aws_sdk_quicksight.types.layout_list

        out["Layouts"] = aws_sdk_quicksight.types.layout_list.serialize_json(
            value["layouts"]
        )
    if "sheet_control_layouts" in value:
        import aws_sdk_quicksight.types.sheet_control_layout_list

        out["SheetControlLayouts"] = (
            aws_sdk_quicksight.types.sheet_control_layout_list.serialize_json(
                value["sheet_control_layouts"]
            )
        )
    if "content_type" in value:
        import aws_sdk_quicksight.types.sheet_content_type

        out["ContentType"] = aws_sdk_quicksight.types.sheet_content_type.serialize_json(
            value["content_type"]
        )
    if "custom_action_defaults" in value:
        import aws_sdk_quicksight.types.visual_custom_action_defaults

        out["CustomActionDefaults"] = (
            aws_sdk_quicksight.types.visual_custom_action_defaults.serialize_json(
                value["custom_action_defaults"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetDefinition:
    out: SheetDefinition = {}  # type: ignore[typeddict-item]
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    else:
        raise DeserializationError("SheetDefinition.sheet_id required")
    if "Title" in data:
        out["title"] = data["Title"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ParameterControls" in data:
        import aws_sdk_quicksight.types.parameter_control_list

        out["parameter_controls"] = (
            aws_sdk_quicksight.types.parameter_control_list.deserialize_json(
                data["ParameterControls"]
            )
        )
    if "FilterControls" in data:
        import aws_sdk_quicksight.types.filter_control_list

        out["filter_controls"] = (
            aws_sdk_quicksight.types.filter_control_list.deserialize_json(
                data["FilterControls"]
            )
        )
    if "Visuals" in data:
        import aws_sdk_quicksight.types.visual_list

        out["visuals"] = aws_sdk_quicksight.types.visual_list.deserialize_json(
            data["Visuals"]
        )
    if "TextBoxes" in data:
        import aws_sdk_quicksight.types.sheet_text_box_list

        out["text_boxes"] = (
            aws_sdk_quicksight.types.sheet_text_box_list.deserialize_json(
                data["TextBoxes"]
            )
        )
    if "Images" in data:
        import aws_sdk_quicksight.types.sheet_image_list

        out["images"] = aws_sdk_quicksight.types.sheet_image_list.deserialize_json(
            data["Images"]
        )
    if "Layouts" in data:
        import aws_sdk_quicksight.types.layout_list

        out["layouts"] = aws_sdk_quicksight.types.layout_list.deserialize_json(
            data["Layouts"]
        )
    if "SheetControlLayouts" in data:
        import aws_sdk_quicksight.types.sheet_control_layout_list

        out["sheet_control_layouts"] = (
            aws_sdk_quicksight.types.sheet_control_layout_list.deserialize_json(
                data["SheetControlLayouts"]
            )
        )
    if "ContentType" in data:
        import aws_sdk_quicksight.types.sheet_content_type

        out["content_type"] = (
            aws_sdk_quicksight.types.sheet_content_type.deserialize_json(
                data["ContentType"]
            )
        )
    if "CustomActionDefaults" in data:
        import aws_sdk_quicksight.types.visual_custom_action_defaults

        out["custom_action_defaults"] = (
            aws_sdk_quicksight.types.visual_custom_action_defaults.deserialize_json(
                data["CustomActionDefaults"]
            )
        )
    return out
