"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovCslgAtom``."""

from typing import Literal, TypeAlias, cast

"""When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools."""
MovCslgAtom: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MovCslgAtom) -> str:
    return value


def deserialize_json(data: str) -> MovCslgAtom:
    return cast(MovCslgAtom, data)
