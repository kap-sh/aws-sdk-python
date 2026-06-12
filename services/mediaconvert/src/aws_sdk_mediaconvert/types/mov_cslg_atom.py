"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovCslgAtom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools."""
MovCslgAtom: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: MovCslgAtom) -> str:
    return value


def deserialize_json(data: str) -> MovCslgAtom:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MovCslgAtom value: {data!r}")
    return cast(MovCslgAtom, data)
