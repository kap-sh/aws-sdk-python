"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_execution_id
    import aws_sdk_codepipeline.types.action_name


class ActionContext(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codepipeline.types.action_name.ActionName"]
    """<p>The name of the action in the context of a job.</p>"""
    action_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.action_execution_id.ActionExecutionId"
    ]
    """<p>The system-generated unique ID that corresponds to an action's execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionContext) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionContext:
    out: ActionContext = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "actionExecutionId" in data:
        out["action_execution_id"] = data["actionExecutionId"]
    return out
