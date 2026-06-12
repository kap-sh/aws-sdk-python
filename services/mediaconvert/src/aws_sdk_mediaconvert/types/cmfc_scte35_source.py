"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcScte35Source``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output."""
CmfcScte35Source: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "NONE",
    )
)


def serialize_json(value: CmfcScte35Source) -> str:
    return value


def deserialize_json(data: str) -> CmfcScte35Source:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmfcScte35Source value: {data!r}")
    return cast(CmfcScte35Source, data)
