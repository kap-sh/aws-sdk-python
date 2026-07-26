"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

DocumentStatus: TypeAlias = Literal[
    "RECEIVED",
    "PROCESSING",
    "INDEXED",
    "UPDATED",
    "FAILED",
    "DELETING",
    "DELETED",
    "DOCUMENT_FAILED_TO_INDEX",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentStatus) -> str:
    return value


def deserialize_json(data: str) -> DocumentStatus:
    return cast(DocumentStatus, data)
