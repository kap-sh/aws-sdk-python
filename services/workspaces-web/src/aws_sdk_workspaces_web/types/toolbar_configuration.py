"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ToolbarConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.hidden_toolbar_item_list
    import aws_sdk_workspaces_web.types.max_display_resolution
    import aws_sdk_workspaces_web.types.toolbar_type
    import aws_sdk_workspaces_web.types.visual_mode


class ToolbarConfiguration(TypedDict, closed=True):
    toolbar_type: NotRequired["aws_sdk_workspaces_web.types.toolbar_type.ToolbarType"]
    """<p>The type of toolbar displayed during the session.</p>"""
    visual_mode: NotRequired["aws_sdk_workspaces_web.types.visual_mode.VisualMode"]
    """<p>The visual mode of the toolbar.</p>"""
    hidden_toolbar_items: NotRequired[
        "aws_sdk_workspaces_web.types.hidden_toolbar_item_list.HiddenToolbarItemList"
    ]
    """<p>The list of toolbar items to be hidden.</p>"""
    max_display_resolution: NotRequired[
        "aws_sdk_workspaces_web.types.max_display_resolution.MaxDisplayResolution"
    ]
    """<p>The maximum display resolution that is allowed for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolbarConfiguration) -> dict:
    out: dict = {}
    if "toolbar_type" in value:
        out["toolbarType"] = value["toolbar_type"]
    if "visual_mode" in value:
        out["visualMode"] = value["visual_mode"]
    if "hidden_toolbar_items" in value:
        import aws_sdk_workspaces_web.types.hidden_toolbar_item_list

        out["hiddenToolbarItems"] = (
            aws_sdk_workspaces_web.types.hidden_toolbar_item_list.serialize_json(
                value["hidden_toolbar_items"]
            )
        )
    if "max_display_resolution" in value:
        out["maxDisplayResolution"] = value["max_display_resolution"]
    return out


def deserialize_json(data: dict) -> ToolbarConfiguration:
    out: ToolbarConfiguration = {}  # type: ignore[typeddict-item]
    if "toolbarType" in data:
        out["toolbar_type"] = data["toolbarType"]
    if "visualMode" in data:
        out["visual_mode"] = data["visualMode"]
    if "hiddenToolbarItems" in data:
        import aws_sdk_workspaces_web.types.hidden_toolbar_item_list

        out["hidden_toolbar_items"] = (
            aws_sdk_workspaces_web.types.hidden_toolbar_item_list.deserialize_json(
                data["hiddenToolbarItems"]
            )
        )
    if "maxDisplayResolution" in data:
        out["max_display_resolution"] = data["maxDisplayResolution"]
    return out
