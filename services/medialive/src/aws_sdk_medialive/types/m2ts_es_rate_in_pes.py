"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsEsRateInPes``."""

from typing import Literal, TypeAlias, cast

"""M2ts Es Rate In Pes"""
M2tsEsRateInPes: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsEsRateInPes) -> str:
    return value


def deserialize_json(data: str) -> M2tsEsRateInPes:
    return cast(M2tsEsRateInPes, data)
