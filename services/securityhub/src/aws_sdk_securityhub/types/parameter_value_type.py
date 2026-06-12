"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ParameterValueType: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "CUSTOM",
    )
)


def serialize_json(value: ParameterValueType) -> str:
    return value


def deserialize_json(data: str) -> ParameterValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterValueType value: {data!r}")
    return cast(ParameterValueType, data)
