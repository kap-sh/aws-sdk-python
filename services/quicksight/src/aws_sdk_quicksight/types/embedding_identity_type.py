"""Generated from Smithy shape ``com.amazonaws.quicksight#EmbeddingIdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

EmbeddingIdentityType: TypeAlias = Literal[
    "IAM",
    "QUICKSIGHT",
    "ANONYMOUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "QUICKSIGHT",
        "ANONYMOUS",
    )
)


def serialize_json(value: EmbeddingIdentityType) -> str:
    return value


def deserialize_json(data: str) -> EmbeddingIdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmbeddingIdentityType value: {data!r}")
    return cast(EmbeddingIdentityType, data)
