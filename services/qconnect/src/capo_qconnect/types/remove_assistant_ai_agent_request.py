"""Generated from Smithy shape ``com.amazonaws.qconnect#RemoveAssistantAIAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_type
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_or_arn


class RemoveAssistantAIAgentRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType"
    """<p>The type of the AI Agent being removed for use by default from the Amazon Q in Connect Assistant.</p>"""
    orchestrator_use_case: NotRequired[
        "capo_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>The orchestrator use case for the AI Agent being removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAssistantAIAgentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveAssistantAIAgentRequest:
    out: RemoveAssistantAIAgentRequest = {}  # type: ignore[typeddict-item]
    return out
