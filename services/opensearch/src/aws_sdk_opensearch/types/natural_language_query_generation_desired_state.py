"""Generated from Smithy shape ``com.amazonaws.opensearch#NaturalLanguageQueryGenerationDesiredState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

NaturalLanguageQueryGenerationDesiredState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: NaturalLanguageQueryGenerationDesiredState) -> str:
    return value


def deserialize_json(data: str) -> NaturalLanguageQueryGenerationDesiredState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NaturalLanguageQueryGenerationDesiredState value: {data!r}"
        )
    return cast(NaturalLanguageQueryGenerationDesiredState, data)
