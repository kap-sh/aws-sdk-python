"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailRegexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_regex

GuardrailRegexes: TypeAlias = list["capo_bedrock.types.guardrail_regex.GuardrailRegex"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexes) -> list:
    import capo_bedrock.types.guardrail_regex

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_regex.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailRegexes:
    import capo_bedrock.types.guardrail_regex

    out: GuardrailRegexes = []
    for item in data:
        out.append(capo_bedrock.types.guardrail_regex.deserialize_json(item))
    return out
