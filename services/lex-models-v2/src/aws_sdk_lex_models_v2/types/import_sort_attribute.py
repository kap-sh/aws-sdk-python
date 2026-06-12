"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ImportSortAttribute: TypeAlias = Literal["LastUpdatedDateTime",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LastUpdatedDateTime",))


def serialize_json(value: ImportSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> ImportSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportSortAttribute value: {data!r}")
    return cast(ImportSortAttribute, data)
