"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ExportStreamSessionFilesOutput``."""

from typing_extensions import TypedDict


class ExportStreamSessionFilesOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ExportStreamSessionFilesOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportStreamSessionFilesOutput:
    out: ExportStreamSessionFilesOutput = {}  # type: ignore[typeddict-item]
    return out
