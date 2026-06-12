"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#LibraryIngestionJobOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""DataAutomationLibraryIngestionJob operation type"""
LibraryIngestionJobOperationType: TypeAlias = Literal[
    "UPSERT",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPSERT",
        "DELETE",
    )
)


def serialize_json(value: LibraryIngestionJobOperationType) -> str:
    return value


def deserialize_json(data: str) -> LibraryIngestionJobOperationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LibraryIngestionJobOperationType value: {data!r}"
        )
    return cast(LibraryIngestionJobOperationType, data)
