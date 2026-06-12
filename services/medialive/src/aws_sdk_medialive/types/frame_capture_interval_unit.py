"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureIntervalUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Frame Capture Interval Unit"""
FrameCaptureIntervalUnit: TypeAlias = Literal[
    "MILLISECONDS",
    "SECONDS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MILLISECONDS",
        "SECONDS",
    )
)


def serialize_json(value: FrameCaptureIntervalUnit) -> str:
    return value


def deserialize_json(data: str) -> FrameCaptureIntervalUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FrameCaptureIntervalUnit value: {data!r}")
    return cast(FrameCaptureIntervalUnit, data)
