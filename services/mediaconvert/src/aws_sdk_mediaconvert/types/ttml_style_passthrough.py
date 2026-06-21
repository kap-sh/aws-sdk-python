"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlStylePassthrough``."""

from typing import Literal, TypeAlias, cast

"""Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output."""
TtmlStylePassthrough: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlStylePassthrough) -> str:
    return value


def deserialize_json(data: str) -> TtmlStylePassthrough:
    return cast(TtmlStylePassthrough, data)
