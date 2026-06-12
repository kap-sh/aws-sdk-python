"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

AcceleratorType: TypeAlias = Literal["gpu",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("gpu",))


def serialize_json(value: AcceleratorType) -> str:
    return value


def deserialize_json(data: str) -> AcceleratorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorType value: {data!r}")
    return cast(AcceleratorType, data)
