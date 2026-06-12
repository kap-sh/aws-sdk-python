"""Generated from Smithy shape ``com.amazonaws.sesv2#ReviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

ReviewStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "GRANTED",
    "DENIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FAILED",
        "GRANTED",
        "DENIED",
    )
)


def serialize_json(value: ReviewStatus) -> str:
    return value


def deserialize_json(data: str) -> ReviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewStatus value: {data!r}")
    return cast(ReviewStatus, data)
