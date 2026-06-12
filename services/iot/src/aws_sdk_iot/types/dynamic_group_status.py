"""Generated from Smithy shape ``com.amazonaws.iot#DynamicGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DynamicGroupStatus: TypeAlias = Literal[
    "ACTIVE",
    "BUILDING",
    "REBUILDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "BUILDING",
        "REBUILDING",
    )
)


def serialize_json(value: DynamicGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> DynamicGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DynamicGroupStatus value: {data!r}")
    return cast(DynamicGroupStatus, data)
