"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

IngestionType: TypeAlias = Literal["auditLog",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("auditLog",))


def serialize_json(value: IngestionType) -> str:
    return value


def deserialize_json(data: str) -> IngestionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionType value: {data!r}")
    return cast(IngestionType, data)
