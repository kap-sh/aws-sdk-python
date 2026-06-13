"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisTargetStatusReason: TypeAlias = Literal[
    "SCAN_IN_PROGRESS",
    "UNSUPPORTED_OS",
    "SSM_UNMANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCAN_IN_PROGRESS",
        "UNSUPPORTED_OS",
        "SSM_UNMANAGED",
    )
)


def serialize_json(value: CisTargetStatusReason) -> str:
    return value


def deserialize_json(data: str) -> CisTargetStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisTargetStatusReason value: {data!r}")
    return cast(CisTargetStatusReason, data)
