"""Generated from Smithy shape ``com.amazonaws.databrew#ParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

ParameterType: TypeAlias = Literal[
    "Datetime",
    "Number",
    "String",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Datetime",
        "Number",
        "String",
    )
)


def serialize_json(value: ParameterType) -> str:
    return value


def deserialize_json(data: str) -> ParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterType value: {data!r}")
    return cast(ParameterType, data)
