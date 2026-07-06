"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAssistantAIAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_data


class UpdateAssistantAIAgentResponse(TypedDict, closed=True):
    assistant: NotRequired["aws_sdk_qconnect.types.assistant_data.AssistantData"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssistantAIAgentResponse) -> dict:
    out: dict = {}
    if "assistant" in value:
        import aws_sdk_qconnect.types.assistant_data

        out["assistant"] = aws_sdk_qconnect.types.assistant_data.serialize_json(
            value["assistant"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssistantAIAgentResponse:
    out: UpdateAssistantAIAgentResponse = {}  # type: ignore[typeddict-item]
    if "assistant" in data:
        import aws_sdk_qconnect.types.assistant_data

        out["assistant"] = aws_sdk_qconnect.types.assistant_data.deserialize_json(
            data["assistant"]
        )
    return out
