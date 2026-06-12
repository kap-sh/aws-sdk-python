"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

CoverageStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_json(value: CoverageStatus) -> str:
    return value


def deserialize_json(data: str) -> CoverageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoverageStatus value: {data!r}")
    return cast(CoverageStatus, data)
