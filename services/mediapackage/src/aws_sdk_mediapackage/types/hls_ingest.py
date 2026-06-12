"""Generated from Smithy shape ``com.amazonaws.mediapackage#HlsIngest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__list_of_ingest_endpoint


class HlsIngest(TypedDict):
    ingest_endpoints: NotRequired[
        "aws_sdk_mediapackage.types.__list_of_ingest_endpoint.__listOfIngestEndpoint"
    ]
    """A list of endpoints to which the source stream should be sent."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsIngest) -> dict:
    out: dict = {}
    if "ingest_endpoints" in value:
        import aws_sdk_mediapackage.types.__list_of_ingest_endpoint

        out["ingestEndpoints"] = (
            aws_sdk_mediapackage.types.__list_of_ingest_endpoint.serialize_json(
                value["ingest_endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsIngest:
    out: HlsIngest = {}  # type: ignore[typeddict-item]
    if "ingestEndpoints" in data:
        import aws_sdk_mediapackage.types.__list_of_ingest_endpoint

        out["ingest_endpoints"] = (
            aws_sdk_mediapackage.types.__list_of_ingest_endpoint.deserialize_json(
                data["ingestEndpoints"]
            )
        )
    return out
