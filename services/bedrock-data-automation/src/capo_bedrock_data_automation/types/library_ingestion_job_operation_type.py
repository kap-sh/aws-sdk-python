"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#LibraryIngestionJobOperationType``."""

from typing import Literal, TypeAlias, cast

"""DataAutomationLibraryIngestionJob operation type"""
LibraryIngestionJobOperationType: TypeAlias = Literal[
    "UPSERT",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LibraryIngestionJobOperationType) -> str:
    return value


def deserialize_json(data: str) -> LibraryIngestionJobOperationType:
    return cast(LibraryIngestionJobOperationType, data)
