"""Generated from Smithy shape ``com.amazonaws.mediapackage#HlsIngest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__list_of_ingest_endpoint


class HlsIngest(TypedDict, closed=True):
    ingest_endpoints: NotRequired[
        "capo_mediapackage.types.__list_of_ingest_endpoint.__listOfIngestEndpoint"
    ]
    """A list of endpoints to which the source stream should be sent."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsIngest) -> dict:
    out: dict = {}
    if "ingest_endpoints" in value:
        import capo_mediapackage.types.__list_of_ingest_endpoint

        out["ingestEndpoints"] = (
            capo_mediapackage.types.__list_of_ingest_endpoint.serialize_json(
                value["ingest_endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsIngest:
    out: HlsIngest = {}  # type: ignore[typeddict-item]
    if "ingestEndpoints" in data:
        import capo_mediapackage.types.__list_of_ingest_endpoint

        out["ingest_endpoints"] = (
            capo_mediapackage.types.__list_of_ingest_endpoint.deserialize_json(
                data["ingestEndpoints"]
            )
        )
    return out
