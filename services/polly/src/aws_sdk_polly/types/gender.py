"""Generated from Smithy shape ``com.amazonaws.polly#Gender``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

Gender: TypeAlias = Literal[
    "Female",
    "Male",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Female",
        "Male",
    )
)


def serialize_json(value: Gender) -> str:
    return value


def deserialize_json(data: str) -> Gender:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Gender value: {data!r}")
    return cast(Gender, data)
