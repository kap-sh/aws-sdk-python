"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265MvOverPictureBoundaries``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If you are setting up the picture as a tile, you must set this to \"disabled\". In all other configurations, you typically enter \"enabled\"."""
H265MvOverPictureBoundaries: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: H265MvOverPictureBoundaries) -> str:
    return value


def deserialize_json(data: str) -> H265MvOverPictureBoundaries:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265MvOverPictureBoundaries value: {data!r}"
        )
    return cast(H265MvOverPictureBoundaries, data)
