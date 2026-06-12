"""Generated from Smithy shape ``com.amazonaws.amplify#Stage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

Stage: TypeAlias = Literal[
    "PRODUCTION",
    "BETA",
    "DEVELOPMENT",
    "EXPERIMENTAL",
    "PULL_REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRODUCTION",
        "BETA",
        "DEVELOPMENT",
        "EXPERIMENTAL",
        "PULL_REQUEST",
    )
)


def serialize_json(value: Stage) -> str:
    return value


def deserialize_json(data: str) -> Stage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Stage value: {data!r}")
    return cast(Stage, data)
