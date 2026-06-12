"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

ValidatorType: TypeAlias = Literal[
    "JSON_SCHEMA",
    "LAMBDA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON_SCHEMA",
        "LAMBDA",
    )
)


def serialize_json(value: ValidatorType) -> str:
    return value


def deserialize_json(data: str) -> ValidatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidatorType value: {data!r}")
    return cast(ValidatorType, data)
