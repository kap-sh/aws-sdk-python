"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMImportJobProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.import_configuration
    import aws_sdk_medical_imaging.types.job_id
    import aws_sdk_medical_imaging.types.job_name
    import aws_sdk_medical_imaging.types.job_status
    import aws_sdk_medical_imaging.types.message
    import aws_sdk_medical_imaging.types.role_arn
    import aws_sdk_medical_imaging.types.s3_uri


class DICOMImportJobProperties(TypedDict):
    job_id: "aws_sdk_medical_imaging.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_name: "aws_sdk_medical_imaging.types.job_name.JobName"
    """<p>The import job name.</p>"""
    job_status: "aws_sdk_medical_imaging.types.job_status.JobStatus"
    """<p>The filters for listing import jobs based on status.</p>"""
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    data_access_role_arn: "aws_sdk_medical_imaging.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) that grants permissions to access medical imaging resources.</p>"""
    ended_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp for when the import job was ended.</p>"""
    submitted_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp for when the import job was submitted.</p>"""
    input_s3_uri: "aws_sdk_medical_imaging.types.s3_uri.S3Uri"
    """<p>The input prefix path for the S3 bucket that contains the DICOM P10 files to be imported.</p>"""
    output_s3_uri: "aws_sdk_medical_imaging.types.s3_uri.S3Uri"
    """<p>The output prefix of the S3 bucket to upload the results of the DICOM import job.</p>"""
    message: NotRequired["aws_sdk_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an import job fails.</p>"""
    import_configuration: NotRequired[
        "aws_sdk_medical_imaging.types.import_configuration.ImportConfiguration"
    ]
    """<p>The object containing <code>DicomJsonMetadataImportConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMImportJobProperties) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobName"] = value["job_name"]
    import aws_sdk_medical_imaging.types.job_status

    out["jobStatus"] = aws_sdk_medical_imaging.types.job_status.serialize_json(
        value["job_status"]
    )
    out["datastoreId"] = value["datastore_id"]
    out["dataAccessRoleArn"] = value["data_access_role_arn"]
    if "ended_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["endedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["ended_at"]
        )
    if "submitted_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["submittedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["submitted_at"]
        )
    out["inputS3Uri"] = value["input_s3_uri"]
    out["outputS3Uri"] = value["output_s3_uri"]
    if "message" in value:
        out["message"] = value["message"]
    if "import_configuration" in value:
        import aws_sdk_medical_imaging.types.import_configuration

        out["importConfiguration"] = (
            aws_sdk_medical_imaging.types.import_configuration.serialize_json(
                value["import_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DICOMImportJobProperties:
    out: DICOMImportJobProperties = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("DICOMImportJobProperties.job_id required")
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("DICOMImportJobProperties.job_name required")
    if "jobStatus" in data:
        import aws_sdk_medical_imaging.types.job_status

        out["job_status"] = aws_sdk_medical_imaging.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("DICOMImportJobProperties.job_status required")
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("DICOMImportJobProperties.datastore_id required")
    if "dataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    else:
        raise DeserializationError(
            "DICOMImportJobProperties.data_access_role_arn required"
        )
    if "endedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["ended_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["endedAt"]
        )
    if "submittedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["submitted_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["submittedAt"]
        )
    if "inputS3Uri" in data:
        out["input_s3_uri"] = data["inputS3Uri"]
    else:
        raise DeserializationError("DICOMImportJobProperties.input_s3_uri required")
    if "outputS3Uri" in data:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        raise DeserializationError("DICOMImportJobProperties.output_s3_uri required")
    if "message" in data:
        out["message"] = data["message"]
    if "importConfiguration" in data:
        import aws_sdk_medical_imaging.types.import_configuration

        out["import_configuration"] = (
            aws_sdk_medical_imaging.types.import_configuration.deserialize_json(
                data["importConfiguration"]
            )
        )
    return out
