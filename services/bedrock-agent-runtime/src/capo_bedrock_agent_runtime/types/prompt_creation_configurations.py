"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PromptCreationConfigurations``."""

from typing_extensions import NotRequired, TypedDict


class PromptCreationConfigurations(TypedDict, closed=True):
    previous_conversation_turns_to_include: NotRequired["int"]
    """<p>The number of previous conversations from the ongoing agent session to include in the conversation history of the agent prompt, during the current invocation. This gives you more granular control over the context that the model is made aware of, and helps the model remove older context which is no longer useful during the ongoing agent session.</p>"""
    exclude_previous_thinking_steps: "bool"
    """<p>If <code>true</code>, the service removes any content between <code>&lt;thinking&gt;</code> tags from previous conversations in an agent session. The service will only remove content from already processed turns. This helps you remove content which might not be useful for current and subsequent invocations. This can reduce the input token count and potentially save costs. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptCreationConfigurations) -> dict:
    out: dict = {}
    if "previous_conversation_turns_to_include" in value:
        out["previousConversationTurnsToInclude"] = value[
            "previous_conversation_turns_to_include"
        ]
    out["excludePreviousThinkingSteps"] = value.get(
        "exclude_previous_thinking_steps", False
    )
    return out


def deserialize_json(data: dict) -> PromptCreationConfigurations:
    out: PromptCreationConfigurations = {}  # type: ignore[typeddict-item]
    if data.get("previousConversationTurnsToInclude") is not None:
        out["previous_conversation_turns_to_include"] = data[
            "previousConversationTurnsToInclude"
        ]
    if data.get("excludePreviousThinkingSteps") is not None:
        out["exclude_previous_thinking_steps"] = data["excludePreviousThinkingSteps"]
    else:
        out["exclude_previous_thinking_steps"] = False
    return out
