"""Generated from Smithy shape ``com.amazonaws.deadline#UsageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UsageType: TypeAlias = Literal[
    "COMPUTE",
    "LICENSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPUTE",
        "LICENSE",
    )
)


def serialize_json(value: UsageType) -> str:
    return value


def deserialize_json(data: str) -> UsageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageType value: {data!r}")
    return cast(UsageType, data)
