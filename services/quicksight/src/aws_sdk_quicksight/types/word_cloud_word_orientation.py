"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordOrientation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

WordCloudWordOrientation: TypeAlias = Literal[
    "HORIZONTAL",
    "HORIZONTAL_AND_VERTICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HORIZONTAL",
        "HORIZONTAL_AND_VERTICAL",
    )
)


def serialize_json(value: WordCloudWordOrientation) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordOrientation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WordCloudWordOrientation value: {data!r}")
    return cast(WordCloudWordOrientation, data)
