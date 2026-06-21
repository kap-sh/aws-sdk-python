"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentStatusType``."""

from typing import Literal, TypeAlias, cast

DocumentStatusType: TypeAlias = Literal[
    "INITIALIZED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentStatusType) -> str:
    return value


def deserialize_json(data: str) -> DocumentStatusType:
    return cast(DocumentStatusType, data)
