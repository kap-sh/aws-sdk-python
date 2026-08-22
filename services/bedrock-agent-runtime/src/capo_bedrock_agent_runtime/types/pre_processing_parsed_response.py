"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PreProcessingParsedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rationale_string


class PreProcessingParsedResponse(TypedDict, closed=True):
    rationale: NotRequired[
        "capo_bedrock_agent_runtime.types.rationale_string.RationaleString"
    ]
    """<p>The text returned by the parsing of the pre-processing step, explaining the steps that the agent plans to take in orchestration, if the user input is valid.</p>"""
    is_valid: NotRequired["bool"]
    """<p>Whether the user input is valid or not. If <code>false</code>, the agent doesn't proceed to orchestration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreProcessingParsedResponse) -> dict:
    out: dict = {}
    if "rationale" in value:
        out["rationale"] = value["rationale"]
    if "is_valid" in value:
        out["isValid"] = value["is_valid"]
    return out


def deserialize_json(data: dict) -> PreProcessingParsedResponse:
    out: PreProcessingParsedResponse = {}  # type: ignore[typeddict-item]
    if data.get("rationale") is not None:
        out["rationale"] = data["rationale"]
    if data.get("isValid") is not None:
        out["is_valid"] = data["isValid"]
    return out
