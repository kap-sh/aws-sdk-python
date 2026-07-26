"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_content_filter

GuardrailContentFilters: TypeAlias = list[
    "capo_bedrock.types.guardrail_content_filter.GuardrailContentFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilters) -> list:
    import capo_bedrock.types.guardrail_content_filter

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_content_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailContentFilters:
    import capo_bedrock.types.guardrail_content_filter

    out: GuardrailContentFilters = []
    for item in data:
        out.append(capo_bedrock.types.guardrail_content_filter.deserialize_json(item))
    return out
