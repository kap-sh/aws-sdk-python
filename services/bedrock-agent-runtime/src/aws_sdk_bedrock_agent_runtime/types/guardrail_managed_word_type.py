"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailManagedWordType``."""

from typing import Literal, TypeAlias, cast

GuardrailManagedWordType: TypeAlias = Literal["PROFANITY",]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailManagedWordType:
    return cast(GuardrailManagedWordType, data)
