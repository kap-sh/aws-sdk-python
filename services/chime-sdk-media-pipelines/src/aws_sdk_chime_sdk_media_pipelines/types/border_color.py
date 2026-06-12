"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#BorderColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

BorderColor: TypeAlias = Literal[
    "Black",
    "Blue",
    "Red",
    "Green",
    "White",
    "Yellow",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Black",
        "Blue",
        "Red",
        "Green",
        "White",
        "Yellow",
    )
)


def serialize_json(value: BorderColor) -> str:
    return value


def deserialize_json(data: str) -> BorderColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BorderColor value: {data!r}")
    return cast(BorderColor, data)
