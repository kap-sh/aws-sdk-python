"""Generated from Smithy shape ``com.amazonaws.appfabric#UpdateIngestionDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.destination_configuration
    import aws_sdk_appfabric.types.identifier


class UpdateIngestionDestinationRequest(TypedDict, closed=True):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""
    ingestion_destination_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>"""
    destination_configuration: (
        "aws_sdk_appfabric.types.destination_configuration.DestinationConfiguration"
    )
    """<p>Contains information about the destination of ingested data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngestionDestinationRequest) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.destination_configuration

    out["destinationConfiguration"] = (
        aws_sdk_appfabric.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIngestionDestinationRequest:
    out: UpdateIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
    if "destinationConfiguration" in data:
        import aws_sdk_appfabric.types.destination_configuration

        out["destination_configuration"] = (
            aws_sdk_appfabric.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIngestionDestinationRequest.destination_configuration required"
        )
    return out
