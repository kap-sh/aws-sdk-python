"""Generated from Smithy shape ``com.amazonaws.databrew#SendProjectSessionActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_databrew.types.client_session_id
    import aws_sdk_databrew.types.preview
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.recipe_step
    import aws_sdk_databrew.types.step_index
    import aws_sdk_databrew.types.view_frame


class SendProjectSessionActionRequest(TypedDict):
    preview: "aws_sdk_databrew.types.preview.Preview"
    """<p>If true, the result of the recipe step will be returned, but not applied.</p>"""
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project to apply the action to.</p>"""
    recipe_step: NotRequired["aws_sdk_databrew.types.recipe_step.RecipeStep"]
    step_index: NotRequired["aws_sdk_databrew.types.step_index.StepIndex"]
    """<p>The index from which to preview a step. This index is used to preview the result of steps that have already been applied, so that the resulting view frame is from earlier in the view frame stack.</p>"""
    client_session_id: NotRequired[
        "aws_sdk_databrew.types.client_session_id.ClientSessionId"
    ]
    """<p>A unique identifier for an interactive session that's currently open and ready for work. The action will be performed on this session.</p>"""
    view_frame: NotRequired["aws_sdk_databrew.types.view_frame.ViewFrame"]


# --- restJson1 ser/de ---
def serialize_json(value: SendProjectSessionActionRequest) -> dict:
    out: dict = {}
    out["Preview"] = value.get("preview", False)
    if "recipe_step" in value:
        import aws_sdk_databrew.types.recipe_step

        out["RecipeStep"] = aws_sdk_databrew.types.recipe_step.serialize_json(
            value["recipe_step"]
        )
    if "step_index" in value:
        out["StepIndex"] = value["step_index"]
    if "client_session_id" in value:
        out["ClientSessionId"] = value["client_session_id"]
    if "view_frame" in value:
        import aws_sdk_databrew.types.view_frame

        out["ViewFrame"] = aws_sdk_databrew.types.view_frame.serialize_json(
            value["view_frame"]
        )
    return out


def deserialize_json(data: dict) -> SendProjectSessionActionRequest:
    out: SendProjectSessionActionRequest = {}  # type: ignore[typeddict-item]
    if "Preview" in data:
        out["preview"] = data["Preview"]
    else:
        out["preview"] = False
    if "RecipeStep" in data:
        import aws_sdk_databrew.types.recipe_step

        out["recipe_step"] = aws_sdk_databrew.types.recipe_step.deserialize_json(
            data["RecipeStep"]
        )
    if "StepIndex" in data:
        out["step_index"] = data["StepIndex"]
    if "ClientSessionId" in data:
        out["client_session_id"] = data["ClientSessionId"]
    if "ViewFrame" in data:
        import aws_sdk_databrew.types.view_frame

        out["view_frame"] = aws_sdk_databrew.types.view_frame.deserialize_json(
            data["ViewFrame"]
        )
    return out
