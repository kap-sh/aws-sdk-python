"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#IngestEndpoint``."""

from typing import TypedDict

from typing_extensions import NotRequired


class IngestEndpoint(TypedDict):
    id: NotRequired["str"]
    """<p>The system-generated unique identifier for the IngestEndpoint.</p>"""
    url: NotRequired["str"]
    """<p>The ingest domain URL where the source stream should be sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> IngestEndpoint:
    out: IngestEndpoint = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
