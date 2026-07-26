"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AgentTurnSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_set_agent_prompt


class AgentTurnSpecification(TypedDict, closed=True):
    agent_prompt: "capo_lex_models_v2.types.test_set_agent_prompt.TestSetAgentPrompt"
    """<p>The agent prompt for the agent turn in a test set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentTurnSpecification) -> dict:
    out: dict = {}
    out["agentPrompt"] = value["agent_prompt"]
    return out


def deserialize_json(data: dict) -> AgentTurnSpecification:
    out: AgentTurnSpecification = {}  # type: ignore[typeddict-item]
    if "agentPrompt" in data:
        out["agent_prompt"] = data["agentPrompt"]
    else:
        raise DeserializationError("AgentTurnSpecification.agent_prompt required")
    return out
