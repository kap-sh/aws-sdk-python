"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordCasing``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

WordCloudWordCasing: TypeAlias = Literal[
    "LOWER_CASE",
    "EXISTING_CASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOWER_CASE",
        "EXISTING_CASE",
    )
)


def serialize_json(value: WordCloudWordCasing) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordCasing:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WordCloudWordCasing value: {data!r}")
    return cast(WordCloudWordCasing, data)
