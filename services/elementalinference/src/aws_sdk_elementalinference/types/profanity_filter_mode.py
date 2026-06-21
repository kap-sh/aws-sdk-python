"""Generated from Smithy shape ``com.amazonaws.elementalinference#ProfanityFilterMode``."""

from typing import Literal, TypeAlias, cast

ProfanityFilterMode: TypeAlias = Literal[
    "DISABLED",
    "CENSOR",
    "DROP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfanityFilterMode) -> str:
    return value


def deserialize_json(data: str) -> ProfanityFilterMode:
    return cast(ProfanityFilterMode, data)
