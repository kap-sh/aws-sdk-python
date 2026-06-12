"""Generated from Smithy shape ``com.amazonaws.medialive#CmafKLVBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Cmaf KLVBehavior"""
CmafKLVBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PASSTHROUGH",
        "PASSTHROUGH",
    )
)


def serialize_json(value: CmafKLVBehavior) -> str:
    return value


def deserialize_json(data: str) -> CmafKLVBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafKLVBehavior value: {data!r}")
    return cast(CmafKLVBehavior, data)
