"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParsingPrompt``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.parsing_prompt_text


class ParsingPrompt(TypedDict, closed=True):
    parsing_prompt_text: (
        "capo_bedrock_agent.types.parsing_prompt_text.ParsingPromptText"
    )
    """<p>Instructions for interpreting the contents of a document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsingPrompt) -> dict:
    out: dict = {}
    out["parsingPromptText"] = value["parsing_prompt_text"]
    return out


def deserialize_json(data: dict) -> ParsingPrompt:
    out: ParsingPrompt = {}  # type: ignore[typeddict-item]
    if "parsingPromptText" in data:
        out["parsing_prompt_text"] = data["parsingPromptText"]
    else:
        raise DeserializationError("ParsingPrompt.parsing_prompt_text required")
    return out
