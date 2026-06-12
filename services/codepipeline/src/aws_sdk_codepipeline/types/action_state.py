"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_execution
    import aws_sdk_codepipeline.types.action_name
    import aws_sdk_codepipeline.types.action_revision
    import aws_sdk_codepipeline.types.url


class ActionState(TypedDict):
    action_name: NotRequired["aws_sdk_codepipeline.types.action_name.ActionName"]
    """<p>The name of the action.</p>"""
    current_revision: NotRequired[
        "aws_sdk_codepipeline.types.action_revision.ActionRevision"
    ]
    """<p>Represents information about the version (or revision) of an action.</p>"""
    latest_execution: NotRequired[
        "aws_sdk_codepipeline.types.action_execution.ActionExecution"
    ]
    """<p>Represents information about the run of an action.</p>"""
    entity_url: NotRequired["aws_sdk_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the state of the action, such as a deployment group details page.</p>"""
    revision_url: NotRequired["aws_sdk_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the revision, such as a commit details page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionState) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "current_revision" in value:
        import aws_sdk_codepipeline.types.action_revision

        out["currentRevision"] = (
            aws_sdk_codepipeline.types.action_revision.serialize_aws_json_1_1(
                value["current_revision"]
            )
        )
    if "latest_execution" in value:
        import aws_sdk_codepipeline.types.action_execution

        out["latestExecution"] = (
            aws_sdk_codepipeline.types.action_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionState:
    out: ActionState = {}  # type: ignore[typeddict-item]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "currentRevision" in data:
        import aws_sdk_codepipeline.types.action_revision

        out["current_revision"] = (
            aws_sdk_codepipeline.types.action_revision.deserialize_aws_json_1_1(
                data["currentRevision"]
            )
        )
    if "latestExecution" in data:
        import aws_sdk_codepipeline.types.action_execution

        out["latest_execution"] = (
            aws_sdk_codepipeline.types.action_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if "entityUrl" in data:
        out["entity_url"] = data["entityUrl"]
    if "revisionUrl" in data:
        out["revision_url"] = data["revisionUrl"]
    return out
