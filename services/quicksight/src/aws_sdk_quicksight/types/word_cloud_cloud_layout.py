"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudCloudLayout``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

WordCloudCloudLayout: TypeAlias = Literal[
    "FLUID",
    "NORMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLUID",
        "NORMAL",
    )
)


def serialize_json(value: WordCloudCloudLayout) -> str:
    return value


def deserialize_json(data: str) -> WordCloudCloudLayout:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WordCloudCloudLayout value: {data!r}")
    return cast(WordCloudCloudLayout, data)
