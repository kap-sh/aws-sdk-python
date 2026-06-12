"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForUdpOut``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Loss Action For Udp Out"""
InputLossActionForUdpOut: TypeAlias = Literal[
    "DROP_PROGRAM",
    "DROP_TS",
    "EMIT_PROGRAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DROP_PROGRAM",
        "DROP_TS",
        "EMIT_PROGRAM",
    )
)


def serialize_json(value: InputLossActionForUdpOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForUdpOut:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputLossActionForUdpOut value: {data!r}")
    return cast(InputLossActionForUdpOut, data)
