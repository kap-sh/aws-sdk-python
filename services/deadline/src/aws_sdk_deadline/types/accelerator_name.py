"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

AcceleratorName: TypeAlias = Literal[
    "t4",
    "a10g",
    "l4",
    "l40s",
    "rtx-pro-server-6000",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "t4",
        "a10g",
        "l4",
        "l40s",
        "rtx-pro-server-6000",
    )
)


def serialize_json(value: AcceleratorName) -> str:
    return value


def deserialize_json(data: str) -> AcceleratorName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorName value: {data!r}")
    return cast(AcceleratorName, data)
