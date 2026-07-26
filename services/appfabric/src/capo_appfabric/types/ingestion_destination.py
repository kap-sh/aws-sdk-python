"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.arn
    import capo_appfabric.types.date_time
    import capo_appfabric.types.destination_configuration
    import capo_appfabric.types.ingestion_destination_status
    import capo_appfabric.types.processing_configuration


class IngestionDestination(TypedDict, closed=True):
    arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion destination.</p>"""
    ingestion_arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion.</p>"""
    processing_configuration: (
        "capo_appfabric.types.processing_configuration.ProcessingConfiguration"
    )
    """<p>Contains information about how ingested data is processed.</p>"""
    destination_configuration: (
        "capo_appfabric.types.destination_configuration.DestinationConfiguration"
    )
    """<p>Contains information about the destination of ingested data.</p>"""
    status: NotRequired[
        "capo_appfabric.types.ingestion_destination_status.IngestionDestinationStatus"
    ]
    """<p>The state of the ingestion destination.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>Active</code>: The ingestion destination is active and is ready to be used.</p> </li> <li> <p> <code>Failed</code>: The ingestion destination has failed. If the ingestion destination is in this state, you should verify the ingestion destination configuration and try again.</p> </li> </ul>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the ingestion destination.</p> <p>Only present when the <code>status</code> of ingestion destination is <code>Failed</code>.</p>"""
    created_at: NotRequired["capo_appfabric.types.date_time.DateTime"]
    """<p>The timestamp of when the ingestion destination was created.</p>"""
    updated_at: NotRequired["capo_appfabric.types.date_time.DateTime"]
    """<p>The timestamp of when the ingestion destination was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionDestination) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["ingestionArn"] = value["ingestion_arn"]
    import capo_appfabric.types.processing_configuration

    out["processingConfiguration"] = (
        capo_appfabric.types.processing_configuration.serialize_json(
            value["processing_configuration"]
        )
    )
    import capo_appfabric.types.destination_configuration

    out["destinationConfiguration"] = (
        capo_appfabric.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    if "status" in value:
        import capo_appfabric.types.ingestion_destination_status

        out["status"] = (
            capo_appfabric.types.ingestion_destination_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "created_at" in value:
        import capo_appfabric.types.date_time

        out["createdAt"] = capo_appfabric.types.date_time.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_appfabric.types.date_time

        out["updatedAt"] = capo_appfabric.types.date_time.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> IngestionDestination:
    out: IngestionDestination = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IngestionDestination.arn required")
    if "ingestionArn" in data:
        out["ingestion_arn"] = data["ingestionArn"]
    else:
        raise DeserializationError("IngestionDestination.ingestion_arn required")
    if "processingConfiguration" in data:
        import capo_appfabric.types.processing_configuration

        out["processing_configuration"] = (
            capo_appfabric.types.processing_configuration.deserialize_json(
                data["processingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "IngestionDestination.processing_configuration required"
        )
    if "destinationConfiguration" in data:
        import capo_appfabric.types.destination_configuration

        out["destination_configuration"] = (
            capo_appfabric.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "IngestionDestination.destination_configuration required"
        )
    if "status" in data:
        import capo_appfabric.types.ingestion_destination_status

        out["status"] = (
            capo_appfabric.types.ingestion_destination_status.deserialize_json(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createdAt" in data:
        import capo_appfabric.types.date_time

        out["created_at"] = capo_appfabric.types.date_time.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_appfabric.types.date_time

        out["updated_at"] = capo_appfabric.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    return out
