"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForRtmpOut``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Loss Action For Rtmp Out"""
InputLossActionForRtmpOut: TypeAlias = Literal[
    "EMIT_OUTPUT",
    "PAUSE_OUTPUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMIT_OUTPUT",
        "PAUSE_OUTPUT",
    )
)


def serialize_json(value: InputLossActionForRtmpOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForRtmpOut:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputLossActionForRtmpOut value: {data!r}")
    return cast(InputLossActionForRtmpOut, data)
