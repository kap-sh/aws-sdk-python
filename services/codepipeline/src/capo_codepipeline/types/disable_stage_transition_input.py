"""Generated from Smithy shape ``com.amazonaws.codepipeline#DisableStageTransitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.disabled_reason
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.stage_transition_type


class DisableStageTransitionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.</p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage where you want to disable the inbound or outbound transition of artifacts.</p>"""
    transition_type: "capo_codepipeline.types.stage_transition_type.StageTransitionType"
    """<p>Specifies whether artifacts are prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).</p>"""
    reason: "capo_codepipeline.types.disabled_reason.DisabledReason"
    """<p>The reason given to the user that a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableStageTransitionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    import capo_codepipeline.types.stage_transition_type

    out["transitionType"] = (
        capo_codepipeline.types.stage_transition_type.serialize_aws_json_1_1(
            value["transition_type"]
        )
    )
    out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableStageTransitionInput:
    out: DisableStageTransitionInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("DisableStageTransitionInput.pipeline_name required")
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("DisableStageTransitionInput.stage_name required")
    if "transitionType" in data:
        import capo_codepipeline.types.stage_transition_type

        out["transition_type"] = (
            capo_codepipeline.types.stage_transition_type.deserialize_aws_json_1_1(
                data["transitionType"]
            )
        )
    else:
        raise DeserializationError(
            "DisableStageTransitionInput.transition_type required"
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("DisableStageTransitionInput.reason required")
    return out
