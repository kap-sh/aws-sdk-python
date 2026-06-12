"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

ResolutionStrategy: TypeAlias = Literal[
    "OPTIMISTIC_CONCURRENCY",
    "LAMBDA",
    "AUTOMERGE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPTIMISTIC_CONCURRENCY",
        "LAMBDA",
        "AUTOMERGE",
        "NONE",
    )
)


def serialize_json(value: ResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> ResolutionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolutionStrategy value: {data!r}")
    return cast(ResolutionStrategy, data)
