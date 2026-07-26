"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LanguageRuntime``."""

from typing import Literal, TypeAlias, cast

LanguageRuntime: TypeAlias = Literal[
    "nodejs",
    "deno",
    "python",
]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageRuntime) -> str:
    return value


def deserialize_json(data: str) -> LanguageRuntime:
    return cast(LanguageRuntime, data)
