"""Generated from Smithy shape ``com.amazonaws.qbusiness#IndexType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

IndexType: TypeAlias = Literal[
    "ENTERPRISE",
    "STARTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENTERPRISE",
        "STARTER",
    )
)


def serialize_json(value: IndexType) -> str:
    return value


def deserialize_json(data: str) -> IndexType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexType value: {data!r}")
    return cast(IndexType, data)
