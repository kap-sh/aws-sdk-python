"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateMetadataTransferJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_status
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class CreateMetadataTransferJobResponse(TypedDict):
    metadata_transfer_job_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The metadata transfer job Id.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The metadata transfer job ARN.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The The metadata transfer job creation DateTime property.</p>"""
    status: "aws_sdk_iottwinmaker.types.metadata_transfer_job_status.MetadataTransferJobStatus"
    """<p>The metadata transfer job response status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMetadataTransferJobResponse) -> dict:
    out: dict = {}
    out["metadataTransferJobId"] = value["metadata_transfer_job_id"]
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_status

    out["status"] = (
        aws_sdk_iottwinmaker.types.metadata_transfer_job_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMetadataTransferJobResponse:
    out: CreateMetadataTransferJobResponse = {}  # type: ignore[typeddict-item]
    if "metadataTransferJobId" in data:
        out["metadata_transfer_job_id"] = data["metadataTransferJobId"]
    else:
        raise DeserializationError(
            "CreateMetadataTransferJobResponse.metadata_transfer_job_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateMetadataTransferJobResponse.arn required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMetadataTransferJobResponse.creation_date_time required"
        )
    if "status" in data:
        import aws_sdk_iottwinmaker.types.metadata_transfer_job_status

        out["status"] = (
            aws_sdk_iottwinmaker.types.metadata_transfer_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateMetadataTransferJobResponse.status required")
    return out
