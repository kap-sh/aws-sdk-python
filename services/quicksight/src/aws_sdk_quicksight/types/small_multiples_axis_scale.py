"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesAxisScale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SmallMultiplesAxisScale: TypeAlias = Literal[
    "SHARED",
    "INDEPENDENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHARED",
        "INDEPENDENT",
    )
)


def serialize_json(value: SmallMultiplesAxisScale) -> str:
    return value


def deserialize_json(data: str) -> SmallMultiplesAxisScale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SmallMultiplesAxisScale value: {data!r}")
    return cast(SmallMultiplesAxisScale, data)
