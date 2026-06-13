"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.import_job_id
    import aws_sdk_omics.types.import_reference_source_list
    import aws_sdk_omics.types.job_status_message
    import aws_sdk_omics.types.reference_import_job_status
    import aws_sdk_omics.types.reference_store_id
    import aws_sdk_omics.types.role_arn


class GetReferenceImportJobResponse(TypedDict):
    id: "aws_sdk_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""
    role_arn: "aws_sdk_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "aws_sdk_omics.types.reference_import_job_status.ReferenceImportJobStatus"
    """<p>The job's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.job_status_message.JobStatusMessage"
    ]
    """<p>The job's status message.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""
    sources: (
        "aws_sdk_omics.types.import_reference_source_list.ImportReferenceSourceList"
    )
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceImportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["roleArn"] = value["role_arn"]
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
    import aws_sdk_omics.types.import_reference_source_list

    out["sources"] = aws_sdk_omics.types.import_reference_source_list.serialize_json(
        value["sources"]
    )
    return out


def deserialize_json(data: dict) -> GetReferenceImportJobResponse:
    out: GetReferenceImportJobResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReferenceImportJobResponse.id required")
    if "referenceStoreId" in data:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError(
            "GetReferenceImportJobResponse.reference_store_id required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetReferenceImportJobResponse.role_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetReferenceImportJobResponse.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetReferenceImportJobResponse.creation_time required"
        )
    if "completionTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_omics.types._prelude.timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    if "sources" in data:
        import aws_sdk_omics.types.import_reference_source_list

        out["sources"] = (
            aws_sdk_omics.types.import_reference_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("GetReferenceImportJobResponse.sources required")
    return out
