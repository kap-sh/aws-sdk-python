"""Generated from Smithy shape ``com.amazonaws.databrew#SampleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

SampleType: TypeAlias = Literal[
    "FIRST_N",
    "LAST_N",
    "RANDOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIRST_N",
        "LAST_N",
        "RANDOM",
    )
)


def serialize_json(value: SampleType) -> str:
    return value


def deserialize_json(data: str) -> SampleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SampleType value: {data!r}")
    return cast(SampleType, data)
