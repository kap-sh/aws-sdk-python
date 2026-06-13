"""Generated from Smithy shape ``com.amazonaws.qbusiness#SystemMessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

SystemMessageType: TypeAlias = Literal[
    "RESPONSE",
    "GROUNDED_RESPONSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESPONSE",
        "GROUNDED_RESPONSE",
    )
)


def serialize_json(value: SystemMessageType) -> str:
    return value


def deserialize_json(data: str) -> SystemMessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SystemMessageType value: {data!r}")
    return cast(SystemMessageType, data)
