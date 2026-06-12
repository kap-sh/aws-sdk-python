"""Generated from Smithy shape ``com.amazonaws.finspace#ChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

ChangeType: TypeAlias = Literal[
    "PUT",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUT",
        "DELETE",
    )
)


def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeType value: {data!r}")
    return cast(ChangeType, data)
