"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Effect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

Effect: TypeAlias = Literal[
    "Allow",
    "Deny",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allow",
        "Deny",
    )
)


def serialize_json(value: Effect) -> str:
    return value


def deserialize_json(data: str) -> Effect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Effect value: {data!r}")
    return cast(Effect, data)
