"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuadrailAction``."""

from typing import Literal, TypeAlias, cast

GuadrailAction: TypeAlias = Literal[
    "INTERVENED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuadrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuadrailAction:
    return cast(GuadrailAction, data)
