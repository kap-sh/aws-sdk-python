"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetMetadataTransferJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.destination_configuration
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.metadata_transfer_job_progress
    import capo_iottwinmaker.types.metadata_transfer_job_status
    import capo_iottwinmaker.types.role_arn
    import capo_iottwinmaker.types.source_configurations
    import capo_iottwinmaker.types.string
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class GetMetadataTransferJobResponse(TypedDict, closed=True):
    metadata_transfer_job_id: "capo_iottwinmaker.types.id.Id"
    """<p>The metadata transfer job Id.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The metadata transfer job ARN.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The metadata transfer job description.</p>"""
    sources: "capo_iottwinmaker.types.source_configurations.SourceConfigurations"
    """<p>The metadata transfer job's sources.</p>"""
    destination: (
        "capo_iottwinmaker.types.destination_configuration.DestinationConfiguration"
    )
    """<p>The metadata transfer job's destination.</p>"""
    metadata_transfer_job_role: "capo_iottwinmaker.types.role_arn.RoleArn"
    """<p>The metadata transfer job's role.</p>"""
    report_url: NotRequired["capo_iottwinmaker.types.string.String"]
    """<p>The metadata transfer job's report URL.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The metadata transfer job's creation DateTime property.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The metadata transfer job's update DateTime property.</p>"""
    status: (
        "capo_iottwinmaker.types.metadata_transfer_job_status.MetadataTransferJobStatus"
    )
    """<p>The metadata transfer job's status.</p>"""
    progress: NotRequired[
        "capo_iottwinmaker.types.metadata_transfer_job_progress.MetadataTransferJobProgress"
    ]
    """<p>The metadata transfer job's progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataTransferJobResponse) -> dict:
    out: dict = {}
    out["metadataTransferJobId"] = value["metadata_transfer_job_id"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_iottwinmaker.types.source_configurations

    out["sources"] = capo_iottwinmaker.types.source_configurations.serialize_json(
        value["sources"]
    )
    import capo_iottwinmaker.types.destination_configuration

    out["destination"] = (
        capo_iottwinmaker.types.destination_configuration.serialize_json(
            value["destination"]
        )
    )
    out["metadataTransferJobRole"] = value["metadata_transfer_job_role"]
    if "report_url" in value:
        out["reportUrl"] = value["report_url"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    import capo_iottwinmaker.types.metadata_transfer_job_status

    out["status"] = capo_iottwinmaker.types.metadata_transfer_job_status.serialize_json(
        value["status"]
    )
    if "progress" in value:
        import capo_iottwinmaker.types.metadata_transfer_job_progress

        out["progress"] = (
            capo_iottwinmaker.types.metadata_transfer_job_progress.serialize_json(
                value["progress"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetadataTransferJobResponse:
    out: GetMetadataTransferJobResponse = {}  # type: ignore[typeddict-item]
    if "metadataTransferJobId" in data:
        out["metadata_transfer_job_id"] = data["metadataTransferJobId"]
    else:
        raise DeserializationError(
            "GetMetadataTransferJobResponse.metadata_transfer_job_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetMetadataTransferJobResponse.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "sources" in data:
        import capo_iottwinmaker.types.source_configurations

        out["sources"] = capo_iottwinmaker.types.source_configurations.deserialize_json(
            data["sources"]
        )
    else:
        raise DeserializationError("GetMetadataTransferJobResponse.sources required")
    if "destination" in data:
        import capo_iottwinmaker.types.destination_configuration

        out["destination"] = (
            capo_iottwinmaker.types.destination_configuration.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError(
            "GetMetadataTransferJobResponse.destination required"
        )
    if "metadataTransferJobRole" in data:
        out["metadata_transfer_job_role"] = data["metadataTransferJobRole"]
    else:
        raise DeserializationError(
            "GetMetadataTransferJobResponse.metadata_transfer_job_role required"
        )
    if "reportUrl" in data:
        out["report_url"] = data["reportUrl"]
    if "creationDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        raise DeserializationError(
            "GetMetadataTransferJobResponse.creation_date_time required"
        )
    if "updateDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError(
            "GetMetadataTransferJobResponse.update_date_time required"
        )
    if "status" in data:
        import capo_iottwinmaker.types.metadata_transfer_job_status

        out["status"] = (
            capo_iottwinmaker.types.metadata_transfer_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetMetadataTransferJobResponse.status required")
    if "progress" in data:
        import capo_iottwinmaker.types.metadata_transfer_job_progress

        out["progress"] = (
            capo_iottwinmaker.types.metadata_transfer_job_progress.deserialize_json(
                data["progress"]
            )
        )
    return out
