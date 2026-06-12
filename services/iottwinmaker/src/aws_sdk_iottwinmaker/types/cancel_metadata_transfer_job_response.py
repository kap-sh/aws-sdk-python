"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CancelMetadataTransferJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_progress
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_status
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class CancelMetadataTransferJobResponse(TypedDict):
    metadata_transfer_job_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The metadata transfer job Id.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The metadata transfer job ARN.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>Used to update the DateTime property.</p>"""
    status: "aws_sdk_iottwinmaker.types.metadata_transfer_job_status.MetadataTransferJobStatus"
    """<p>The metadata transfer job's status.</p>"""
    progress: NotRequired[
        "aws_sdk_iottwinmaker.types.metadata_transfer_job_progress.MetadataTransferJobProgress"
    ]
    """<p>The metadata transfer job's progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMetadataTransferJobResponse) -> dict:
    out: dict = {}
    out["metadataTransferJobId"] = value["metadata_transfer_job_id"]
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_status

    out["status"] = (
        aws_sdk_iottwinmaker.types.metadata_transfer_job_status.serialize_json(
            value["status"]
        )
    )
    if "progress" in value:
        import aws_sdk_iottwinmaker.types.metadata_transfer_job_progress

        out["progress"] = (
            aws_sdk_iottwinmaker.types.metadata_transfer_job_progress.serialize_json(
                value["progress"]
            )
        )
    return out


def deserialize_json(data: dict) -> CancelMetadataTransferJobResponse:
    out: CancelMetadataTransferJobResponse = {}  # type: ignore[typeddict-item]
    if "metadataTransferJobId" in data:
        out["metadata_transfer_job_id"] = data["metadataTransferJobId"]
    else:
        raise DeserializationError(
            "CancelMetadataTransferJobResponse.metadata_transfer_job_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CancelMetadataTransferJobResponse.arn required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError(
            "CancelMetadataTransferJobResponse.update_date_time required"
        )
    if "status" in data:
        import aws_sdk_iottwinmaker.types.metadata_transfer_job_status

        out["status"] = (
            aws_sdk_iottwinmaker.types.metadata_transfer_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CancelMetadataTransferJobResponse.status required")
    if "progress" in data:
        import aws_sdk_iottwinmaker.types.metadata_transfer_job_progress

        out["progress"] = (
            aws_sdk_iottwinmaker.types.metadata_transfer_job_progress.deserialize_json(
                data["progress"]
            )
        )
    return out
