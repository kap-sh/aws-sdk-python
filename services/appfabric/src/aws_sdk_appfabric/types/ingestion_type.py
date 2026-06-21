"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionType``."""

from typing import Literal, TypeAlias, cast

IngestionType: TypeAlias = Literal["auditLog",]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionType) -> str:
    return value


def deserialize_json(data: str) -> IngestionType:
    return cast(IngestionType, data)
