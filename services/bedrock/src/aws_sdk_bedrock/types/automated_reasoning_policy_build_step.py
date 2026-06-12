"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStep``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_context
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_message_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_element


class AutomatedReasoningPolicyBuildStep(TypedDict):
    context: "aws_sdk_bedrock.types.automated_reasoning_policy_build_step_context.AutomatedReasoningPolicyBuildStepContext"
    """<p>Contextual information about what was being processed during this build step, such as the type of operation or the source material being analyzed.</p>"""
    prior_element: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_element.AutomatedReasoningPolicyDefinitionElement"
    ]
    """<p>Reference to the previous element or step in the build process, helping to trace the sequence of operations.</p>"""
    messages: "aws_sdk_bedrock.types.automated_reasoning_policy_build_step_message_list.AutomatedReasoningPolicyBuildStepMessageList"
    """<p>A list of messages generated during this build step, including informational messages, warnings, and error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStep) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_context

    out["context"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_step_context.serialize_json(
            value["context"]
        )
    )
    if "prior_element" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_element

        out["priorElement"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_element.serialize_json(
                value["prior_element"]
            )
        )
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_message_list

    out["messages"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_step_message_list.serialize_json(
            value["messages"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildStep:
    out: AutomatedReasoningPolicyBuildStep = {}  # type: ignore[typeddict-item]
    if "context" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_context

        out["context"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_step_context.deserialize_json(
                data["context"]
            )
        )
    else:
        raise DeserializationError("AutomatedReasoningPolicyBuildStep.context required")
    if "priorElement" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_element

        out["prior_element"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_element.deserialize_json(
                data["priorElement"]
            )
        )
    if "messages" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_step_message_list

        out["messages"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_step_message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildStep.messages required"
        )
    return out
