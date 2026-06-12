"""Generated from Smithy shape ``com.amazonaws.polly#Engine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

Engine: TypeAlias = Literal[
    "standard",
    "neural",
    "long-form",
    "generative",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "neural",
        "long-form",
        "generative",
    )
)


def serialize_json(value: Engine) -> str:
    return value


def deserialize_json(data: str) -> Engine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Engine value: {data!r}")
    return cast(Engine, data)
