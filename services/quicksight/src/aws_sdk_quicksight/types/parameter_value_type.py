"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ParameterValueType: TypeAlias = Literal[
    "MULTI_VALUED",
    "SINGLE_VALUED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_VALUED",
        "SINGLE_VALUED",
    )
)


def serialize_json(value: ParameterValueType) -> str:
    return value


def deserialize_json(data: str) -> ParameterValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterValueType value: {data!r}")
    return cast(ParameterValueType, data)
