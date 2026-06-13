"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericFilterSelectAllOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NumericFilterSelectAllOptions: TypeAlias = Literal["FILTER_ALL_VALUES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FILTER_ALL_VALUES",))


def serialize_json(value: NumericFilterSelectAllOptions) -> str:
    return value


def deserialize_json(data: str) -> NumericFilterSelectAllOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NumericFilterSelectAllOptions value: {data!r}"
        )
    return cast(NumericFilterSelectAllOptions, data)
