"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ViewContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.view_actions
    import aws_sdk_connectparticipant.types.view_input_schema
    import aws_sdk_connectparticipant.types.view_template


class ViewContent(TypedDict, closed=True):
    input_schema: NotRequired[
        "aws_sdk_connectparticipant.types.view_input_schema.ViewInputSchema"
    ]
    """<p>The schema representing the input data that the view template must be supplied to render.</p>"""
    template: NotRequired["aws_sdk_connectparticipant.types.view_template.ViewTemplate"]
    """<p>The view template representing the structure of the view.</p>"""
    actions: NotRequired["aws_sdk_connectparticipant.types.view_actions.ViewActions"]
    """<p>A list of actions possible from the view</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewContent) -> dict:
    out: dict = {}
    if "input_schema" in value:
        out["InputSchema"] = value["input_schema"]
    if "template" in value:
        out["Template"] = value["template"]
    if "actions" in value:
        import aws_sdk_connectparticipant.types.view_actions

        out["Actions"] = aws_sdk_connectparticipant.types.view_actions.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> ViewContent:
    out: ViewContent = {}  # type: ignore[typeddict-item]
    if "InputSchema" in data:
        out["input_schema"] = data["InputSchema"]
    if "Template" in data:
        out["template"] = data["Template"]
    if "Actions" in data:
        import aws_sdk_connectparticipant.types.view_actions

        out["actions"] = aws_sdk_connectparticipant.types.view_actions.deserialize_json(
            data["Actions"]
        )
    return out
