"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordScaling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

WordCloudWordScaling: TypeAlias = Literal[
    "EMPHASIZE",
    "NORMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMPHASIZE",
        "NORMAL",
    )
)


def serialize_json(value: WordCloudWordScaling) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordScaling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WordCloudWordScaling value: {data!r}")
    return cast(WordCloudWordScaling, data)
