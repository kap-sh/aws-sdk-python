"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#IngestEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.ingest_endpoint

IngestEndpointList: TypeAlias = list[
    "capo_mediapackagev2.types.ingest_endpoint.IngestEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestEndpointList) -> list:
    import capo_mediapackagev2.types.ingest_endpoint

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.ingest_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> IngestEndpointList:
    import capo_mediapackagev2.types.ingest_endpoint

    out: IngestEndpointList = []
    for item in data:
        out.append(capo_mediapackagev2.types.ingest_endpoint.deserialize_json(item))
    return out
