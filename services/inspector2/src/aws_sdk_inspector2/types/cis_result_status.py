"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisResultStatus: TypeAlias = Literal[
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


def serialize_json(value: CisResultStatus) -> str:
    return value


def deserialize_json(data: str) -> CisResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisResultStatus value: {data!r}")
    return cast(CisResultStatus, data)
