"""Generated from Smithy shape ``com.amazonaws.medialive#IFrameOnlyPlaylistType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""When set to \"standard\", an I-Frame only playlist will be written out for each video output in the output group. This I-Frame only playlist will contain byte range offsets pointing to the I-frame(s) in each segment."""
IFrameOnlyPlaylistType: TypeAlias = Literal[
    "DISABLED",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "STANDARD",
    )
)


def serialize_json(value: IFrameOnlyPlaylistType) -> str:
    return value


def deserialize_json(data: str) -> IFrameOnlyPlaylistType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IFrameOnlyPlaylistType value: {data!r}")
    return cast(IFrameOnlyPlaylistType, data)
