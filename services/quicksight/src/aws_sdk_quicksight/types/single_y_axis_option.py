"""Generated from Smithy shape ``com.amazonaws.quicksight#SingleYAxisOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SingleYAxisOption: TypeAlias = Literal["PRIMARY_Y_AXIS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PRIMARY_Y_AXIS",))


def serialize_json(value: SingleYAxisOption) -> str:
    return value


def deserialize_json(data: str) -> SingleYAxisOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SingleYAxisOption value: {data!r}")
    return cast(SingleYAxisOption, data)
