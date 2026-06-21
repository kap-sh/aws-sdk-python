"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsEsRateInPes``."""

from typing import Literal, TypeAlias, cast

"""Controls whether to include the ES Rate field in the PES header."""
M2tsEsRateInPes: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsEsRateInPes) -> str:
    return value


def deserialize_json(data: str) -> M2tsEsRateInPes:
    return cast(M2tsEsRateInPes, data)
