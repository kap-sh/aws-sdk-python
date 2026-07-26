"""Generated from Smithy shape ``com.amazonaws.mediapackage#IngestEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.sensitive_string


class IngestEndpoint(TypedDict, closed=True):
    id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The system generated unique identifier for the IngestEndpoint"""
    password: NotRequired["capo_mediapackage.types.sensitive_string.SensitiveString"]
    """The system generated password for ingest authentication."""
    url: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ingest URL to which the source stream should be sent."""
    username: NotRequired["capo_mediapackage.types.sensitive_string.SensitiveString"]
    """The system generated username for ingest authentication."""


# --- restJson1 ser/de ---
def serialize_json(value: IngestEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "password" in value:
        out["password"] = value["password"]
    if "url" in value:
        out["url"] = value["url"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> IngestEndpoint:
    out: IngestEndpoint = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "password" in data:
        out["password"] = data["password"]
    if "url" in data:
        out["url"] = data["url"]
    if "username" in data:
        out["username"] = data["username"]
    return out
