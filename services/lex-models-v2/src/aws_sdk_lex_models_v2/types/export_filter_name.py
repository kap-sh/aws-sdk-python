"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ExportFilterName: TypeAlias = Literal["ExportResourceType",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ExportResourceType",))


def serialize_json(value: ExportFilterName) -> str:
    return value


def deserialize_json(data: str) -> ExportFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportFilterName value: {data!r}")
    return cast(ExportFilterName, data)
