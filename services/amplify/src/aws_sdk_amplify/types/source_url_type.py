"""Generated from Smithy shape ``com.amazonaws.amplify#SourceUrlType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

SourceUrlType: TypeAlias = Literal[
    "ZIP",
    "BUCKET_PREFIX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZIP",
        "BUCKET_PREFIX",
    )
)


def serialize_json(value: SourceUrlType) -> str:
    return value


def deserialize_json(data: str) -> SourceUrlType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceUrlType value: {data!r}")
    return cast(SourceUrlType, data)
