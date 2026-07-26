"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsPcrControl``."""

from typing import Literal, TypeAlias, cast

"""M2ts Pcr Control"""
M2tsPcrControl: TypeAlias = Literal[
    "CONFIGURED_PCR_PERIOD",
    "PCR_EVERY_PES_PACKET",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsPcrControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsPcrControl:
    return cast(M2tsPcrControl, data)
