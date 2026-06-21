"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#LibraryIngestionJobStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of DataAutomationLibraryIngestionJob"""
LibraryIngestionJobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LibraryIngestionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> LibraryIngestionJobStatus:
    return cast(LibraryIngestionJobStatus, data)
