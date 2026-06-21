"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8PcrControl``."""

from typing import Literal, TypeAlias, cast

"""M3u8 Pcr Control"""
M3u8PcrControl: TypeAlias = Literal[
    "CONFIGURED_PCR_PERIOD",
    "PCR_EVERY_PES_PACKET",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8PcrControl) -> str:
    return value


def deserialize_json(data: str) -> M3u8PcrControl:
    return cast(M3u8PcrControl, data)
