"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailManagedWordsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_managed_words_type


class GuardrailManagedWordsConfig(TypedDict):
    type: (
        "aws_sdk_qconnect.types.guardrail_managed_words_type.GuardrailManagedWordsType"
    )
    """<p>The managed word type to configure for the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordsConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> GuardrailManagedWordsConfig:
    out: GuardrailManagedWordsConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GuardrailManagedWordsConfig.type required")
    return out
