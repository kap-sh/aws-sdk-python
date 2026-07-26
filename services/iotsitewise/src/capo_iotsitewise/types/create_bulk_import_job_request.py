"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateBulkImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.adaptive_ingestion
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.delete_files_after_import
    import capo_iotsitewise.types.error_report_location
    import capo_iotsitewise.types.files
    import capo_iotsitewise.types.job_configuration
    import capo_iotsitewise.types.name


class CreateBulkImportJobRequest(TypedDict, closed=True):
    job_name: "capo_iotsitewise.types.name.Name"
    """<p>The unique name that helps identify the job request.</p>"""
    job_role_arn: "capo_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the IAM role that allows IoT SiteWise to read Amazon S3 data.</p>"""
    files: "capo_iotsitewise.types.files.Files"
    """<p>The files in the specified Amazon S3 bucket that contain your data.</p>"""
    error_report_location: (
        "capo_iotsitewise.types.error_report_location.ErrorReportLocation"
    )
    """<p>The Amazon S3 destination where errors associated with the job creation request are saved.</p>"""
    job_configuration: "capo_iotsitewise.types.job_configuration.JobConfiguration"
    """<p>Contains the configuration information of a job, such as the file format used to save data in Amazon S3.</p>"""
    adaptive_ingestion: NotRequired[
        "capo_iotsitewise.types.adaptive_ingestion.AdaptiveIngestion"
    ]
    """<p>If set to true, ingest new data into IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into IoT SiteWise as is.</p>"""
    delete_files_after_import: NotRequired[
        "capo_iotsitewise.types.delete_files_after_import.DeleteFilesAfterImport"
    ]
    """<p>If set to true, your data files is deleted from S3, after ingestion into IoT SiteWise storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBulkImportJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["jobRoleArn"] = value["job_role_arn"]
    import capo_iotsitewise.types.files

    out["files"] = capo_iotsitewise.types.files.serialize_json(value["files"])
    import capo_iotsitewise.types.error_report_location

    out["errorReportLocation"] = (
        capo_iotsitewise.types.error_report_location.serialize_json(
            value["error_report_location"]
        )
    )
    import capo_iotsitewise.types.job_configuration

    out["jobConfiguration"] = capo_iotsitewise.types.job_configuration.serialize_json(
        value["job_configuration"]
    )
    if "adaptive_ingestion" in value:
        out["adaptiveIngestion"] = value["adaptive_ingestion"]
    if "delete_files_after_import" in value:
        out["deleteFilesAfterImport"] = value["delete_files_after_import"]
    return out


def deserialize_json(data: dict) -> CreateBulkImportJobRequest:
    out: CreateBulkImportJobRequest = {}  # type: ignore[typeddict-item]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateBulkImportJobRequest.job_name required")
    if "jobRoleArn" in data:
        out["job_role_arn"] = data["jobRoleArn"]
    else:
        raise DeserializationError("CreateBulkImportJobRequest.job_role_arn required")
    if "files" in data:
        import capo_iotsitewise.types.files

        out["files"] = capo_iotsitewise.types.files.deserialize_json(data["files"])
    else:
        raise DeserializationError("CreateBulkImportJobRequest.files required")
    if "errorReportLocation" in data:
        import capo_iotsitewise.types.error_report_location

        out["error_report_location"] = (
            capo_iotsitewise.types.error_report_location.deserialize_json(
                data["errorReportLocation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBulkImportJobRequest.error_report_location required"
        )
    if "jobConfiguration" in data:
        import capo_iotsitewise.types.job_configuration

        out["job_configuration"] = (
            capo_iotsitewise.types.job_configuration.deserialize_json(
                data["jobConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBulkImportJobRequest.job_configuration required"
        )
    if "adaptiveIngestion" in data:
        out["adaptive_ingestion"] = data["adaptiveIngestion"]
    if "deleteFilesAfterImport" in data:
        out["delete_files_after_import"] = data["deleteFilesAfterImport"]
    return out
