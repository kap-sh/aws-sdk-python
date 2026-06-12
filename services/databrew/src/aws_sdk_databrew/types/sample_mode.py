"""Generated from Smithy shape ``com.amazonaws.databrew#SampleMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

SampleMode: TypeAlias = Literal[
    "FULL_DATASET",
    "CUSTOM_ROWS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_DATASET",
        "CUSTOM_ROWS",
    )
)


def serialize_json(value: SampleMode) -> str:
    return value


def deserialize_json(data: str) -> SampleMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SampleMode value: {data!r}")
    return cast(SampleMode, data)
