"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4CslgAtom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools."""
Mp4CslgAtom: TypeAlias = Literal[
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


def serialize_json(value: Mp4CslgAtom) -> str:
    return value


def deserialize_json(data: str) -> Mp4CslgAtom:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mp4CslgAtom value: {data!r}")
    return cast(Mp4CslgAtom, data)
