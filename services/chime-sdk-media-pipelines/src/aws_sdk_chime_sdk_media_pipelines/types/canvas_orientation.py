"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CanvasOrientation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

CanvasOrientation: TypeAlias = Literal[
    "Landscape",
    "Portrait",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Landscape",
        "Portrait",
    )
)


def serialize_json(value: CanvasOrientation) -> str:
    return value


def deserialize_json(data: str) -> CanvasOrientation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CanvasOrientation value: {data!r}")
    return cast(CanvasOrientation, data)
