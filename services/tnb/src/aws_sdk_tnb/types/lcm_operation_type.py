"""Generated from Smithy shape ``com.amazonaws.tnb#LcmOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

LcmOperationType: TypeAlias = Literal[
    "INSTANTIATE",
    "UPDATE",
    "TERMINATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANTIATE",
        "UPDATE",
        "TERMINATE",
    )
)


def serialize_json(value: LcmOperationType) -> str:
    return value


def deserialize_json(data: str) -> LcmOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LcmOperationType value: {data!r}")
    return cast(LcmOperationType, data)
