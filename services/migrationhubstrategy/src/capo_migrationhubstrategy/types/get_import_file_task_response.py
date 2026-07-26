"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetImportFileTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.import_file_task_status
    import capo_migrationhubstrategy.types.import_s3_bucket
    import capo_migrationhubstrategy.types.import_s3_key
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.string
    import capo_migrationhubstrategy.types.time_stamp


class GetImportFileTaskResponse(TypedDict, closed=True):
    id: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The import file task <code>id</code> returned in the response of <a>StartImportFileTask</a>. </p>"""
    status: NotRequired[
        "capo_migrationhubstrategy.types.import_file_task_status.ImportFileTaskStatus"
    ]
    """<p> Status of import file task. </p>"""
    start_time: NotRequired["capo_migrationhubstrategy.types.time_stamp.TimeStamp"]
    """<p> Start time of the import task. </p>"""
    input_s3_bucket: NotRequired[
        "capo_migrationhubstrategy.types.import_s3_bucket.importS3Bucket"
    ]
    """<p> The S3 bucket where import file is located. </p>"""
    input_s3_key: NotRequired[
        "capo_migrationhubstrategy.types.import_s3_key.importS3Key"
    ]
    """<p> The Amazon S3 key name of the import file. </p>"""
    status_report_s3_bucket: NotRequired[
        "capo_migrationhubstrategy.types.import_s3_bucket.importS3Bucket"
    ]
    """<p> The S3 bucket name for status report of import task. </p>"""
    status_report_s3_key: NotRequired[
        "capo_migrationhubstrategy.types.import_s3_key.importS3Key"
    ]
    """<p> The Amazon S3 key name for status report of import task. The report contains details about whether each record imported successfully or why it did not.</p>"""
    completion_time: NotRequired["capo_migrationhubstrategy.types.time_stamp.TimeStamp"]
    """<p> The time that the import task completed. </p>"""
    number_of_records_success: NotRequired[
        "capo_migrationhubstrategy.types.integer.Integer"
    ]
    """<p> The number of records successfully imported. </p>"""
    number_of_records_failed: NotRequired[
        "capo_migrationhubstrategy.types.integer.Integer"
    ]
    """<p> The number of records that failed to be imported. </p>"""
    import_name: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The name of the import task given in <a>StartImportFileTask</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportFileTaskResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        import capo_migrationhubstrategy.types.time_stamp

        out["startTime"] = capo_migrationhubstrategy.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "input_s3_bucket" in value:
        out["inputS3Bucket"] = value["input_s3_bucket"]
    if "input_s3_key" in value:
        out["inputS3Key"] = value["input_s3_key"]
    if "status_report_s3_bucket" in value:
        out["statusReportS3Bucket"] = value["status_report_s3_bucket"]
    if "status_report_s3_key" in value:
        out["statusReportS3Key"] = value["status_report_s3_key"]
    if "completion_time" in value:
        import capo_migrationhubstrategy.types.time_stamp

        out["completionTime"] = (
            capo_migrationhubstrategy.types.time_stamp.serialize_json(
                value["completion_time"]
            )
        )
    if "number_of_records_success" in value:
        out["numberOfRecordsSuccess"] = value["number_of_records_success"]
    if "number_of_records_failed" in value:
        out["numberOfRecordsFailed"] = value["number_of_records_failed"]
    if "import_name" in value:
        out["importName"] = value["import_name"]
    return out


def deserialize_json(data: dict) -> GetImportFileTaskResponse:
    out: GetImportFileTaskResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "startTime" in data:
        import capo_migrationhubstrategy.types.time_stamp

        out["start_time"] = capo_migrationhubstrategy.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if "inputS3Bucket" in data:
        out["input_s3_bucket"] = data["inputS3Bucket"]
    if "inputS3Key" in data:
        out["input_s3_key"] = data["inputS3Key"]
    if "statusReportS3Bucket" in data:
        out["status_report_s3_bucket"] = data["statusReportS3Bucket"]
    if "statusReportS3Key" in data:
        out["status_report_s3_key"] = data["statusReportS3Key"]
    if "completionTime" in data:
        import capo_migrationhubstrategy.types.time_stamp

        out["completion_time"] = (
            capo_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["completionTime"]
            )
        )
    if "numberOfRecordsSuccess" in data:
        out["number_of_records_success"] = data["numberOfRecordsSuccess"]
    if "numberOfRecordsFailed" in data:
        out["number_of_records_failed"] = data["numberOfRecordsFailed"]
    if "importName" in data:
        out["import_name"] = data["importName"]
    return out
