"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

UtteranceContentType: TypeAlias = Literal[
    "PlainText",
    "CustomPayload",
    "SSML",
    "ImageResponseCard",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PlainText",
        "CustomPayload",
        "SSML",
        "ImageResponseCard",
    )
)


def serialize_json(value: UtteranceContentType) -> str:
    return value


def deserialize_json(data: str) -> UtteranceContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UtteranceContentType value: {data!r}")
    return cast(UtteranceContentType, data)
