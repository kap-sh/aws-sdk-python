"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTextCharactersCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.text_characters_guarded
    import capo_bedrock_runtime.types.text_characters_total


class GuardrailTextCharactersCoverage(TypedDict, closed=True):
    guarded: NotRequired[
        "capo_bedrock_runtime.types.text_characters_guarded.TextCharactersGuarded"
    ]
    """<p>The text characters that were guarded by the guardrail coverage.</p>"""
    total: NotRequired[
        "capo_bedrock_runtime.types.text_characters_total.TextCharactersTotal"
    ]
    """<p>The total text characters by the guardrail coverage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTextCharactersCoverage) -> dict:
    out: dict = {}
    if "guarded" in value:
        out["guarded"] = value["guarded"]
    if "total" in value:
        out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> GuardrailTextCharactersCoverage:
    out: GuardrailTextCharactersCoverage = {}  # type: ignore[typeddict-item]
    if data.get("guarded") is not None:
        out["guarded"] = data["guarded"]
    if data.get("total") is not None:
        out["total"] = data["total"]
    return out
