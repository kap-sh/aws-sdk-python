"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterNullOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FilterNullOption: TypeAlias = Literal[
    "ALL_VALUES",
    "NULLS_ONLY",
    "NON_NULLS_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_VALUES",
        "NULLS_ONLY",
        "NON_NULLS_ONLY",
    )
)


def serialize_json(value: FilterNullOption) -> str:
    return value


def deserialize_json(data: str) -> FilterNullOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterNullOption value: {data!r}")
    return cast(FilterNullOption, data)
