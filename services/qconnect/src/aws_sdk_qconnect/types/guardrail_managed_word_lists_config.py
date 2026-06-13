"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailManagedWordListsConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_managed_words_config

GuardrailManagedWordListsConfig: TypeAlias = list[
    "aws_sdk_qconnect.types.guardrail_managed_words_config.GuardrailManagedWordsConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordListsConfig) -> list:
    import aws_sdk_qconnect.types.guardrail_managed_words_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.guardrail_managed_words_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailManagedWordListsConfig:
    import aws_sdk_qconnect.types.guardrail_managed_words_config

    out: GuardrailManagedWordListsConfig = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.guardrail_managed_words_config.deserialize_json(item)
        )
    return out
