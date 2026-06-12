"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForMsSmoothOut``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Loss Action For Ms Smooth Out"""
InputLossActionForMsSmoothOut: TypeAlias = Literal[
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


def serialize_json(value: InputLossActionForMsSmoothOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForMsSmoothOut:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InputLossActionForMsSmoothOut value: {data!r}"
        )
    return cast(InputLossActionForMsSmoothOut, data)
