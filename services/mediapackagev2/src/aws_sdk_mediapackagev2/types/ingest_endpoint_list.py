"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#IngestEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.ingest_endpoint

IngestEndpointList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.ingest_endpoint.IngestEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestEndpointList) -> list:
    import aws_sdk_mediapackagev2.types.ingest_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackagev2.types.ingest_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> IngestEndpointList:
    import aws_sdk_mediapackagev2.types.ingest_endpoint

    out: IngestEndpointList = []
    for item in data:
        out.append(aws_sdk_mediapackagev2.types.ingest_endpoint.deserialize_json(item))
    return out
