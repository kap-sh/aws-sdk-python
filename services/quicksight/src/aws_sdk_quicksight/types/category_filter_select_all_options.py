"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterSelectAllOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CategoryFilterSelectAllOptions: TypeAlias = Literal["FILTER_ALL_VALUES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FILTER_ALL_VALUES",))


def serialize_json(value: CategoryFilterSelectAllOptions) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterSelectAllOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CategoryFilterSelectAllOptions value: {data!r}"
        )
    return cast(CategoryFilterSelectAllOptions, data)
