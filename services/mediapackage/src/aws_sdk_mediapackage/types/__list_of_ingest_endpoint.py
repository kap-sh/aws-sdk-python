"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfIngestEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.ingest_endpoint

__listOfIngestEndpoint: TypeAlias = list[
    "aws_sdk_mediapackage.types.ingest_endpoint.IngestEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIngestEndpoint) -> list:
    import aws_sdk_mediapackage.types.ingest_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackage.types.ingest_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIngestEndpoint:
    import aws_sdk_mediapackage.types.ingest_endpoint

    out: __listOfIngestEndpoint = []
    for item in data:
        out.append(aws_sdk_mediapackage.types.ingest_endpoint.deserialize_json(item))
    return out
