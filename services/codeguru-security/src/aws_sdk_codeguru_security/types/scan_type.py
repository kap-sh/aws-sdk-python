"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_security.errors import DeserializationError

ScanType: TypeAlias = Literal[
    "Standard",
    "Express",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "Express",
    )
)


def serialize_json(value: ScanType) -> str:
    return value


def deserialize_json(data: str) -> ScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanType value: {data!r}")
    return cast(ScanType, data)
