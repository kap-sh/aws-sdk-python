"""Generated from Smithy shape ``com.amazonaws.databrew#DatabaseOutputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

DatabaseOutputMode: TypeAlias = Literal["NEW_TABLE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NEW_TABLE",))


def serialize_json(value: DatabaseOutputMode) -> str:
    return value


def deserialize_json(data: str) -> DatabaseOutputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseOutputMode value: {data!r}")
    return cast(DatabaseOutputMode, data)
