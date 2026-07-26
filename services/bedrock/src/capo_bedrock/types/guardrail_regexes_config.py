"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailRegexesConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_regex_config

GuardrailRegexesConfig: TypeAlias = list[
    "capo_bedrock.types.guardrail_regex_config.GuardrailRegexConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexesConfig) -> list:
    import capo_bedrock.types.guardrail_regex_config

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_regex_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailRegexesConfig:
    import capo_bedrock.types.guardrail_regex_config

    out: GuardrailRegexesConfig = []
    for item in data:
        out.append(capo_bedrock.types.guardrail_regex_config.deserialize_json(item))
    return out
