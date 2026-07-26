"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupportedLanguages``."""

from typing import Literal, TypeAlias, cast

SupportedLanguages: TypeAlias = Literal["Python_3",]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedLanguages) -> str:
    return value


def deserialize_json(data: str) -> SupportedLanguages:
    return cast(SupportedLanguages, data)
