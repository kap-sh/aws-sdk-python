"""Generated from Smithy shape ``com.amazonaws.quicksight#TargetVisualOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TargetVisualOptions: TypeAlias = Literal["ALL_VISUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL_VISUALS",))


def serialize_json(value: TargetVisualOptions) -> str:
    return value


def deserialize_json(data: str) -> TargetVisualOptions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetVisualOptions value: {data!r}")
    return cast(TargetVisualOptions, data)
