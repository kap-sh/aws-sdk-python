"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TranscriptFormat``."""

from typing import Literal, TypeAlias, cast

TranscriptFormat: TypeAlias = Literal["Lex",]


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptFormat) -> str:
    return value


def deserialize_json(data: str) -> TranscriptFormat:
    return cast(TranscriptFormat, data)
