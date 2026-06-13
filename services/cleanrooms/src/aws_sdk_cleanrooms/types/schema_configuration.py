"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

SchemaConfiguration: TypeAlias = Literal["DIFFERENTIAL_PRIVACY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DIFFERENTIAL_PRIVACY",))


def serialize_json(value: SchemaConfiguration) -> str:
    return value


def deserialize_json(data: str) -> SchemaConfiguration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaConfiguration value: {data!r}")
    return cast(SchemaConfiguration, data)
