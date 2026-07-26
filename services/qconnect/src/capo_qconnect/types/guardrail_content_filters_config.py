"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailContentFiltersConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_content_filter_config

GuardrailContentFiltersConfig: TypeAlias = list[
    "capo_qconnect.types.guardrail_content_filter_config.GuardrailContentFilterConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFiltersConfig) -> list:
    import capo_qconnect.types.guardrail_content_filter_config

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.guardrail_content_filter_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailContentFiltersConfig:
    import capo_qconnect.types.guardrail_content_filter_config

    out: GuardrailContentFiltersConfig = []
    for item in data:
        out.append(
            capo_qconnect.types.guardrail_content_filter_config.deserialize_json(item)
        )
    return out
