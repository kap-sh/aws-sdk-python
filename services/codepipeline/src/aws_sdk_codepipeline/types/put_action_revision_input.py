"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutActionRevisionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_name
    import aws_sdk_codepipeline.types.action_revision
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.stage_name


class PutActionRevisionInput(TypedDict):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline that starts processing the revision to the source.</p>"""
    stage_name: "aws_sdk_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage that contains the action that acts on the revision.</p>"""
    action_name: "aws_sdk_codepipeline.types.action_name.ActionName"
    """<p>The name of the action that processes the revision.</p>"""
    action_revision: "aws_sdk_codepipeline.types.action_revision.ActionRevision"
    """<p>Represents information about the version (or revision) of an action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutActionRevisionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["actionName"] = value["action_name"]
    import aws_sdk_codepipeline.types.action_revision

    out["actionRevision"] = (
        aws_sdk_codepipeline.types.action_revision.serialize_aws_json_1_1(
            value["action_revision"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutActionRevisionInput:
    out: PutActionRevisionInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("PutActionRevisionInput.pipeline_name required")
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("PutActionRevisionInput.stage_name required")
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    else:
        raise DeserializationError("PutActionRevisionInput.action_name required")
    if "actionRevision" in data:
        import aws_sdk_codepipeline.types.action_revision

        out["action_revision"] = (
            aws_sdk_codepipeline.types.action_revision.deserialize_aws_json_1_1(
                data["actionRevision"]
            )
        )
    else:
        raise DeserializationError("PutActionRevisionInput.action_revision required")
    return out
