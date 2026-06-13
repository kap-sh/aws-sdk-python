"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScanState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_security.errors import DeserializationError

ScanState: TypeAlias = Literal[
    "InProgress",
    "Successful",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Successful",
        "Failed",
    )
)


def serialize_json(value: ScanState) -> str:
    return value


def deserialize_json(data: str) -> ScanState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanState value: {data!r}")
    return cast(ScanState, data)
