"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ExportSortAttribute: TypeAlias = Literal["LastUpdatedDateTime",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LastUpdatedDateTime",))


def serialize_json(value: ExportSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> ExportSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportSortAttribute value: {data!r}")
    return cast(ExportSortAttribute, data)
