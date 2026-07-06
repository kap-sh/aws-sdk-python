"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.import_job_id
    import aws_sdk_omics.types.reference_import_job_status
    import aws_sdk_omics.types.reference_store_id
    import aws_sdk_omics.types.role_arn


class ImportReferenceJobItem(TypedDict, closed=True):
    id: "aws_sdk_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""
    role_arn: "aws_sdk_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "aws_sdk_omics.types.reference_import_job_status.ReferenceImportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceJobItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["roleArn"] = value["role_arn"]
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


def deserialize_json(data: dict) -> ImportReferenceJobItem:
    out: ImportReferenceJobItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ImportReferenceJobItem.id required")
    if "referenceStoreId" in data:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError("ImportReferenceJobItem.reference_store_id required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ImportReferenceJobItem.role_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportReferenceJobItem.status required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ImportReferenceJobItem.creation_time required")
    if "completionTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_omics.types._prelude.timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    return out
