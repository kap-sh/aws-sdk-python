"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265MvTemporalPredictor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If you are setting up the picture as a tile, you must set this to \"disabled\". In other configurations, you typically enter \"enabled\"."""
H265MvTemporalPredictor: TypeAlias = Literal[
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


def serialize_json(value: H265MvTemporalPredictor) -> str:
    return value


def deserialize_json(data: str) -> H265MvTemporalPredictor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265MvTemporalPredictor value: {data!r}")
    return cast(H265MvTemporalPredictor, data)
