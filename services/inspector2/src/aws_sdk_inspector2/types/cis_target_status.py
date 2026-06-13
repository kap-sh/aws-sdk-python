"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisTargetStatus: TypeAlias = Literal[
    "TIMED_OUT",
    "CANCELLED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TIMED_OUT",
        "CANCELLED",
        "COMPLETED",
    )
)


def serialize_json(value: CisTargetStatus) -> str:
    return value


def deserialize_json(data: str) -> CisTargetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisTargetStatus value: {data!r}")
    return cast(CisTargetStatus, data)
