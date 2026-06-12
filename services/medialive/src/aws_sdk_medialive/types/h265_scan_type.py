"""Generated from Smithy shape ``com.amazonaws.medialive#H265ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Scan Type"""
H265ScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERLACED",
        "PROGRESSIVE",
    )
)


def serialize_json(value: H265ScanType) -> str:
    return value


def deserialize_json(data: str) -> H265ScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265ScanType value: {data!r}")
    return cast(H265ScanType, data)
