"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

DocumentStatus: TypeAlias = Literal[
    "INDEXED",
    "PARTIALLY_INDEXED",
    "PENDING",
    "FAILED",
    "METADATA_PARTIALLY_INDEXED",
    "METADATA_UPDATE_FAILED",
    "IGNORED",
    "NOT_FOUND",
    "STARTING",
    "IN_PROGRESS",
    "DELETING",
    "DELETE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentStatus) -> str:
    return value


def deserialize_json(data: str) -> DocumentStatus:
    return cast(DocumentStatus, data)
