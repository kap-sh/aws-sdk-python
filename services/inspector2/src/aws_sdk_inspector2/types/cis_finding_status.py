"""Generated from Smithy shape ``com.amazonaws.inspector2#CisFindingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisFindingStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "SKIPPED",
    )
)


def serialize_json(value: CisFindingStatus) -> str:
    return value


def deserialize_json(data: str) -> CisFindingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisFindingStatus value: {data!r}")
    return cast(CisFindingStatus, data)
