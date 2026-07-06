"""Generated from Smithy shape ``com.amazonaws.mediapackage#RotateIngestEndpointCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class RotateIngestEndpointCredentialsRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the channel the IngestEndpoint is on."""
    ingest_endpoint_id: "aws_sdk_mediapackage.types.__string.__string"
    """The id of the IngestEndpoint whose credentials should be rotated"""


# --- restJson1 ser/de ---
def serialize_json(value: RotateIngestEndpointCredentialsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RotateIngestEndpointCredentialsRequest:
    out: RotateIngestEndpointCredentialsRequest = {}  # type: ignore[typeddict-item]
    return out
