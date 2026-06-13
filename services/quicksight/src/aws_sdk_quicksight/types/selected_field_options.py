"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedFieldOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SelectedFieldOptions: TypeAlias = Literal["ALL_FIELDS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL_FIELDS",))


def serialize_json(value: SelectedFieldOptions) -> str:
    return value


def deserialize_json(data: str) -> SelectedFieldOptions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectedFieldOptions value: {data!r}")
    return cast(SelectedFieldOptions, data)
