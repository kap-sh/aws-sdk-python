"""Generated from Smithy shape ``com.amazonaws.opensearch#NaturalLanguageQueryGenerationCurrentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

NaturalLanguageQueryGenerationCurrentState: TypeAlias = Literal[
    "NOT_ENABLED",
    "ENABLE_COMPLETE",
    "ENABLE_IN_PROGRESS",
    "ENABLE_FAILED",
    "DISABLE_COMPLETE",
    "DISABLE_IN_PROGRESS",
    "DISABLE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_ENABLED",
        "ENABLE_COMPLETE",
        "ENABLE_IN_PROGRESS",
        "ENABLE_FAILED",
        "DISABLE_COMPLETE",
        "DISABLE_IN_PROGRESS",
        "DISABLE_FAILED",
    )
)


def serialize_json(value: NaturalLanguageQueryGenerationCurrentState) -> str:
    return value


def deserialize_json(data: str) -> NaturalLanguageQueryGenerationCurrentState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NaturalLanguageQueryGenerationCurrentState value: {data!r}"
        )
    return cast(NaturalLanguageQueryGenerationCurrentState, data)
