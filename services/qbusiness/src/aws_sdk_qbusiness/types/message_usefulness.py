"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageUsefulness``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

MessageUsefulness: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USEFUL",
        "NOT_USEFUL",
    )
)


def serialize_json(value: MessageUsefulness) -> str:
    return value


def deserialize_json(data: str) -> MessageUsefulness:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageUsefulness value: {data!r}")
    return cast(MessageUsefulness, data)
