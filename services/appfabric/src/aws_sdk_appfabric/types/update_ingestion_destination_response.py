"""Generated from Smithy shape ``com.amazonaws.appfabric#UpdateIngestionDestinationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.ingestion_destination


class UpdateIngestionDestinationResponse(TypedDict):
    ingestion_destination: (
        "aws_sdk_appfabric.types.ingestion_destination.IngestionDestination"
    )
    """<p>Contains information about an ingestion destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngestionDestinationResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.ingestion_destination

    out["ingestionDestination"] = (
        aws_sdk_appfabric.types.ingestion_destination.serialize_json(
            value["ingestion_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIngestionDestinationResponse:
    out: UpdateIngestionDestinationResponse = {}  # type: ignore[typeddict-item]
    if "ingestionDestination" in data:
        import aws_sdk_appfabric.types.ingestion_destination

        out["ingestion_destination"] = (
            aws_sdk_appfabric.types.ingestion_destination.deserialize_json(
                data["ingestionDestination"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIngestionDestinationResponse.ingestion_destination required"
        )
    return out
