"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ExportStatus``."""

from typing import Literal, TypeAlias, cast

"""The current state of the export. Current possible values include : PENDING - export request received, IN_PROGRESS - export is being processed, SUCCEEDED - export completed successfully, and FAILED - export encountered an error."""
ExportStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
