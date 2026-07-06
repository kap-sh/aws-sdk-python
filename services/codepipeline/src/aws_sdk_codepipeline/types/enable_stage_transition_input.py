"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnableStageTransitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.stage_name
    import aws_sdk_codepipeline.types.stage_transition_type


class EnableStageTransitionInput(TypedDict, closed=True):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.</p>"""
    stage_name: "aws_sdk_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).</p>"""
    transition_type: (
        "aws_sdk_codepipeline.types.stage_transition_type.StageTransitionType"
    )
    """<p>Specifies whether artifacts are allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already processed artifacts are allowed to transition to the next stage (outbound).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableStageTransitionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    import aws_sdk_codepipeline.types.stage_transition_type

    out["transitionType"] = (
        aws_sdk_codepipeline.types.stage_transition_type.serialize_aws_json_1_1(
            value["transition_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableStageTransitionInput:
    out: EnableStageTransitionInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("EnableStageTransitionInput.pipeline_name required")
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("EnableStageTransitionInput.stage_name required")
    if "transitionType" in data:
        import aws_sdk_codepipeline.types.stage_transition_type

        out["transition_type"] = (
            aws_sdk_codepipeline.types.stage_transition_type.deserialize_aws_json_1_1(
                data["transitionType"]
            )
        )
    else:
        raise DeserializationError(
            "EnableStageTransitionInput.transition_type required"
        )
    return out
