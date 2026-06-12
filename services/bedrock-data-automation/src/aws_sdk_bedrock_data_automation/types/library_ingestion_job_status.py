"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#LibraryIngestionJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Status of DataAutomationLibraryIngestionJob"""
LibraryIngestionJobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "FAILED",
    )
)


def serialize_json(value: LibraryIngestionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> LibraryIngestionJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LibraryIngestionJobStatus value: {data!r}")
    return cast(LibraryIngestionJobStatus, data)
