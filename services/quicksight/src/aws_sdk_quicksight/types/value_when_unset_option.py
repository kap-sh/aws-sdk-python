"""Generated from Smithy shape ``com.amazonaws.quicksight#ValueWhenUnsetOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ValueWhenUnsetOption: TypeAlias = Literal[
    "RECOMMENDED_VALUE",
    "NULL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECOMMENDED_VALUE",
        "NULL",
    )
)


def serialize_json(value: ValueWhenUnsetOption) -> str:
    return value


def deserialize_json(data: str) -> ValueWhenUnsetOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValueWhenUnsetOption value: {data!r}")
    return cast(ValueWhenUnsetOption, data)
