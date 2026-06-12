"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DiskImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

DiskImageFormat: TypeAlias = Literal[
    "VMDK",
    "RAW",
    "VHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VMDK",
        "RAW",
        "VHD",
    )
)


def serialize_json(value: DiskImageFormat) -> str:
    return value


def deserialize_json(data: str) -> DiskImageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiskImageFormat value: {data!r}")
    return cast(DiskImageFormat, data)
