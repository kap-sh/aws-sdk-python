"""Generated from Smithy shape ``com.amazonaws.qbusiness#ReadAccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ReadAccessType: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_json(value: ReadAccessType) -> str:
    return value


def deserialize_json(data: str) -> ReadAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReadAccessType value: {data!r}")
    return cast(ReadAccessType, data)
