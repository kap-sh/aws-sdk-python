"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeScanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CodeScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED",
        "SKIPPED",
    )
)


def serialize_json(value: CodeScanStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeScanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeScanStatus value: {data!r}")
    return cast(CodeScanStatus, data)
