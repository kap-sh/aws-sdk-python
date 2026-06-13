"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetJobDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.export_job_id
    import aws_sdk_omics.types.read_set_export_job_status
    import aws_sdk_omics.types.s3_destination
    import aws_sdk_omics.types.sequence_store_id


class ExportReadSetJobDetail(TypedDict):
    id: "aws_sdk_omics.types.export_job_id.ExportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    destination: "aws_sdk_omics.types.s3_destination.S3Destination"
    """<p>The job's destination in Amazon S3.</p>"""
    status: "aws_sdk_omics.types.read_set_export_job_status.ReadSetExportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetJobDetail) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["destination"] = value["destination"]
    out["status"] = value["status"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "completion_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["completionTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["completion_time"]
        )
    return out


def deserialize_json(data: dict) -> ExportReadSetJobDetail:
    out: ExportReadSetJobDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ExportReadSetJobDetail.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError("ExportReadSetJobDetail.sequence_store_id required")
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("ExportReadSetJobDetail.destination required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ExportReadSetJobDetail.status required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ExportReadSetJobDetail.creation_time required")
    if "completionTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_omics.types._prelude.timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    return out
