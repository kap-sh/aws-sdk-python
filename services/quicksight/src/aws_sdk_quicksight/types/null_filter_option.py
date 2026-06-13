"""Generated from Smithy shape ``com.amazonaws.quicksight#NullFilterOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NullFilterOption: TypeAlias = Literal[
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


def serialize_json(value: NullFilterOption) -> str:
    return value


def deserialize_json(data: str) -> NullFilterOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NullFilterOption value: {data!r}")
    return cast(NullFilterOption, data)
