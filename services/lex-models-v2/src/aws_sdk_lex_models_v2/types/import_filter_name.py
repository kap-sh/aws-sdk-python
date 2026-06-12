"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ImportFilterName: TypeAlias = Literal["ImportResourceType",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ImportResourceType",))


def serialize_json(value: ImportFilterName) -> str:
    return value


def deserialize_json(data: str) -> ImportFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportFilterName value: {data!r}")
    return cast(ImportFilterName, data)
