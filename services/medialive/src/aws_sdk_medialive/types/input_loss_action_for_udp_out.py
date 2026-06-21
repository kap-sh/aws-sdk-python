"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForUdpOut``."""

from typing import Literal, TypeAlias, cast

"""Input Loss Action For Udp Out"""
InputLossActionForUdpOut: TypeAlias = Literal[
    "DROP_PROGRAM",
    "DROP_TS",
    "EMIT_PROGRAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputLossActionForUdpOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForUdpOut:
    return cast(InputLossActionForUdpOut, data)
