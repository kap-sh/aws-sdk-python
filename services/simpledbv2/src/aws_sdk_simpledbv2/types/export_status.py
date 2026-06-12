"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_simpledbv2.errors import DeserializationError

"""The current state of the export. Current possible values include : PENDING - export request received, IN_PROGRESS - export is being processed, SUCCEEDED - export completed successfully, and FAILED - export encountered an error."""
ExportStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: ExportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportStatus value: {data!r}")
    return cast(ExportStatus, data)
