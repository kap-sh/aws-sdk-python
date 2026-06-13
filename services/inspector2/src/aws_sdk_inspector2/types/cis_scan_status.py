"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisScanStatus: TypeAlias = Literal[
    "FAILED",
    "COMPLETED",
    "CANCELLED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "COMPLETED",
        "CANCELLED",
        "IN_PROGRESS",
    )
)


def serialize_json(value: CisScanStatus) -> str:
    return value


def deserialize_json(data: str) -> CisScanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisScanStatus value: {data!r}")
    return cast(CisScanStatus, data)
