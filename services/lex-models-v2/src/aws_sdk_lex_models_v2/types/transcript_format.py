"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TranscriptFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TranscriptFormat: TypeAlias = Literal["Lex",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Lex",))


def serialize_json(value: TranscriptFormat) -> str:
    return value


def deserialize_json(data: str) -> TranscriptFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscriptFormat value: {data!r}")
    return cast(TranscriptFormat, data)
