"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.export_job_id
    import aws_sdk_omics.types.export_read_set_detail_list
    import aws_sdk_omics.types.job_status_message
    import aws_sdk_omics.types.read_set_export_job_status
    import aws_sdk_omics.types.s3_destination
    import aws_sdk_omics.types.sequence_store_id


class GetReadSetExportJobResponse(TypedDict):
    id: "aws_sdk_omics.types.export_job_id.ExportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    destination: "aws_sdk_omics.types.s3_destination.S3Destination"
    """<p>The job's destination in Amazon S3.</p>"""
    status: "aws_sdk_omics.types.read_set_export_job_status.ReadSetExportJobStatus"
    """<p>The job's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.job_status_message.JobStatusMessage"
    ]
    """<p>The job's status message.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""
    read_sets: NotRequired[
        "aws_sdk_omics.types.export_read_set_detail_list.ExportReadSetDetailList"
    ]
    """<p>The job's read sets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetExportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["destination"] = value["destination"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "completion_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["completionTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["completion_time"]
        )
    if "read_sets" in value:
        import aws_sdk_omics.types.export_read_set_detail_list

        out["readSets"] = (
            aws_sdk_omics.types.export_read_set_detail_list.serialize_json(
                value["read_sets"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetReadSetExportJobResponse:
    out: GetReadSetExportJobResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReadSetExportJobResponse.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "GetReadSetExportJobResponse.sequence_store_id required"
        )
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("GetReadSetExportJobResponse.destination required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetReadSetExportJobResponse.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetReadSetExportJobResponse.creation_time required")
    if "completionTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_omics.types._prelude.timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    if "readSets" in data:
        import aws_sdk_omics.types.export_read_set_detail_list

        out["read_sets"] = (
            aws_sdk_omics.types.export_read_set_detail_list.deserialize_json(
                data["readSets"]
            )
        )
    return out
