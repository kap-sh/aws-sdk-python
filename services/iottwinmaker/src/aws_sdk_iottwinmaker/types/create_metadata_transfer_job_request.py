"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateMetadataTransferJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.destination_configuration
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.source_configurations


class CreateMetadataTransferJobRequest(TypedDict):
    metadata_transfer_job_id: NotRequired["aws_sdk_iottwinmaker.types.id.Id"]
    """<p>The metadata transfer job Id.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The metadata transfer job description.</p>"""
    sources: "aws_sdk_iottwinmaker.types.source_configurations.SourceConfigurations"
    """<p>The metadata transfer job sources.</p>"""
    destination: (
        "aws_sdk_iottwinmaker.types.destination_configuration.DestinationConfiguration"
    )
    """<p>The metadata transfer job destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMetadataTransferJobRequest) -> dict:
    out: dict = {}
    if "metadata_transfer_job_id" in value:
        out["metadataTransferJobId"] = value["metadata_transfer_job_id"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_iottwinmaker.types.source_configurations

    out["sources"] = aws_sdk_iottwinmaker.types.source_configurations.serialize_json(
        value["sources"]
    )
    import aws_sdk_iottwinmaker.types.destination_configuration

    out["destination"] = (
        aws_sdk_iottwinmaker.types.destination_configuration.serialize_json(
            value["destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMetadataTransferJobRequest:
    out: CreateMetadataTransferJobRequest = {}  # type: ignore[typeddict-item]
    if "metadataTransferJobId" in data:
        out["metadata_transfer_job_id"] = data["metadataTransferJobId"]
    if "description" in data:
        out["description"] = data["description"]
    if "sources" in data:
        import aws_sdk_iottwinmaker.types.source_configurations

        out["sources"] = (
            aws_sdk_iottwinmaker.types.source_configurations.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("CreateMetadataTransferJobRequest.sources required")
    if "destination" in data:
        import aws_sdk_iottwinmaker.types.destination_configuration

        out["destination"] = (
            aws_sdk_iottwinmaker.types.destination_configuration.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMetadataTransferJobRequest.destination required"
        )
    return out
