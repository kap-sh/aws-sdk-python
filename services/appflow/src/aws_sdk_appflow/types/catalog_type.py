"""Generated from Smithy shape ``com.amazonaws.appflow#CatalogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

CatalogType: TypeAlias = Literal["GLUE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GLUE",))


def serialize_json(value: CatalogType) -> str:
    return value


def deserialize_json(data: str) -> CatalogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CatalogType value: {data!r}")
    return cast(CatalogType, data)
