"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailManagedWordsType``."""

from typing import Literal, TypeAlias, cast

GuardrailManagedWordsType: TypeAlias = Literal["PROFANITY",]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordsType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailManagedWordsType:
    return cast(GuardrailManagedWordsType, data)
