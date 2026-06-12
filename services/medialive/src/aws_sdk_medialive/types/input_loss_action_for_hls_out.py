"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForHlsOut``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Loss Action For Hls Out"""
InputLossActionForHlsOut: TypeAlias = Literal[
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


def serialize_json(value: InputLossActionForHlsOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForHlsOut:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputLossActionForHlsOut value: {data!r}")
    return cast(InputLossActionForHlsOut, data)
