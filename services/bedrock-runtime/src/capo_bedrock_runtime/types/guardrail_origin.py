"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOrigin``."""

from typing import Literal, TypeAlias, cast

GuardrailOrigin: TypeAlias = Literal[
    "REQUEST",
    "ACCOUNT_ENFORCED",
    "ORGANIZATION_ENFORCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOrigin) -> str:
    return value


def deserialize_json(data: str) -> GuardrailOrigin:
    return cast(GuardrailOrigin, data)
