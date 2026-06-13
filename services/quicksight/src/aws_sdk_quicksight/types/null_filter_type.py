"""Generated from Smithy shape ``com.amazonaws.quicksight#NullFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NullFilterType: TypeAlias = Literal[
    "ALL_VALUES",
    "NON_NULLS_ONLY",
    "NULLS_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_VALUES",
        "NON_NULLS_ONLY",
        "NULLS_ONLY",
    )
)


def serialize_json(value: NullFilterType) -> str:
    return value


def deserialize_json(data: str) -> NullFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NullFilterType value: {data!r}")
    return cast(NullFilterType, data)
