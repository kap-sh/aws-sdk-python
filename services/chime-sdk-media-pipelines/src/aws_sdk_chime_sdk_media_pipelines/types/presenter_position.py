"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#PresenterPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

PresenterPosition: TypeAlias = Literal[
    "TopLeft",
    "TopRight",
    "BottomLeft",
    "BottomRight",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TopLeft",
        "TopRight",
        "BottomLeft",
        "BottomRight",
    )
)


def serialize_json(value: PresenterPosition) -> str:
    return value


def deserialize_json(data: str) -> PresenterPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PresenterPosition value: {data!r}")
    return cast(PresenterPosition, data)
