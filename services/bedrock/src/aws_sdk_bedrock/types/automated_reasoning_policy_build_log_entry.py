"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildLogEntry``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation_status
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_list


class AutomatedReasoningPolicyBuildLogEntry(TypedDict):
    annotation: "aws_sdk_bedrock.types.automated_reasoning_policy_annotation.AutomatedReasoningPolicyAnnotation"
    """<p>The annotation or operation that was being processed when this log entry was created.</p>"""
    status: "aws_sdk_bedrock.types.automated_reasoning_policy_annotation_status.AutomatedReasoningPolicyAnnotationStatus"
    """<p>The status of the build step (e.g., SUCCESS, FAILED, IN_PROGRESS).</p>"""
    build_steps: "aws_sdk_bedrock.types.automated_reasoning_policy_build_step_list.AutomatedReasoningPolicyBuildStepList"
    """<p>Detailed information about the specific build steps that were executed, including any sub-operations or transformations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildLogEntry) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation

    out["annotation"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_annotation.serialize_json(
            value["annotation"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation_status

    out["status"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_annotation_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_list

    out["buildSteps"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_step_list.serialize_json(
            value["build_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildLogEntry:
    out: AutomatedReasoningPolicyBuildLogEntry = {}  # type: ignore[typeddict-item]
    if "annotation" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_annotation

        out["annotation"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_annotation.deserialize_json(
                data["annotation"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildLogEntry.annotation required"
        )
    if "status" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_annotation_status

        out["status"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_annotation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildLogEntry.status required"
        )
    if "buildSteps" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_list

        out["build_steps"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_step_list.deserialize_json(
                data["buildSteps"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildLogEntry.build_steps required"
        )
    return out
