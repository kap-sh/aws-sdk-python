"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailWordsConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_word_config

GuardrailWordsConfig: TypeAlias = list[
    "capo_qconnect.types.guardrail_word_config.GuardrailWordConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordsConfig) -> list:
    import capo_qconnect.types.guardrail_word_config

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.guardrail_word_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailWordsConfig:
    import capo_qconnect.types.guardrail_word_config

    out: GuardrailWordsConfig = []
    for item in data:
        out.append(capo_qconnect.types.guardrail_word_config.deserialize_json(item))
    return out
