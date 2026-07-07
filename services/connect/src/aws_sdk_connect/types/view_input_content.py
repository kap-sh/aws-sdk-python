"""Generated from Smithy shape ``com.amazonaws.connect#ViewInputContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_actions
    import aws_sdk_connect.types.view_template


class ViewInputContent(TypedDict, closed=True):
    template: NotRequired["aws_sdk_connect.types.view_template.ViewTemplate"]
    """<p>The view template representing the structure of the view.</p>"""
    actions: NotRequired["aws_sdk_connect.types.view_actions.ViewActions"]
    """<p>A list of possible actions from the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewInputContent) -> dict:
    out: dict = {}
    if "template" in value:
        out["Template"] = value["template"]
    if "actions" in value:
        import aws_sdk_connect.types.view_actions

        out["Actions"] = aws_sdk_connect.types.view_actions.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> ViewInputContent:
    out: ViewInputContent = {}  # type: ignore[typeddict-item]
    if "Template" in data:
        out["template"] = data["Template"]
    if "Actions" in data:
        import aws_sdk_connect.types.view_actions

        out["actions"] = aws_sdk_connect.types.view_actions.deserialize_json(
            data["Actions"]
        )
    return out
