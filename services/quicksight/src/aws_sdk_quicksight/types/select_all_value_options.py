"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectAllValueOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SelectAllValueOptions: TypeAlias = Literal["ALL_VALUES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL_VALUES",))


def serialize_json(value: SelectAllValueOptions) -> str:
    return value


def deserialize_json(data: str) -> SelectAllValueOptions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectAllValueOptions value: {data!r}")
    return cast(SelectAllValueOptions, data)
