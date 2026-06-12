"""Generated from Smithy shape ``com.amazonaws.medialive#H264ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Scan Type"""
H264ScanType: TypeAlias = Literal[
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


def serialize_json(value: H264ScanType) -> str:
    return value


def deserialize_json(data: str) -> H264ScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264ScanType value: {data!r}")
    return cast(H264ScanType, data)
