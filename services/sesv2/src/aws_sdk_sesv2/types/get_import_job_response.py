"""Generated from Smithy shape ``com.amazonaws.sesv2#GetImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.failed_records_count
    import aws_sdk_sesv2.types.failure_info
    import aws_sdk_sesv2.types.import_data_source
    import aws_sdk_sesv2.types.import_destination
    import aws_sdk_sesv2.types.job_id
    import aws_sdk_sesv2.types.job_status
    import aws_sdk_sesv2.types.processed_records_count
    import aws_sdk_sesv2.types.timestamp


class GetImportJobResponse(TypedDict):
    job_id: NotRequired["aws_sdk_sesv2.types.job_id.JobId"]
    """<p>A string that represents the import job ID.</p>"""
    import_destination: NotRequired[
        "aws_sdk_sesv2.types.import_destination.ImportDestination"
    ]
    """<p>The destination of the import job.</p>"""
    import_data_source: NotRequired[
        "aws_sdk_sesv2.types.import_data_source.ImportDataSource"
    ]
    """<p>The data source of the import job.</p>"""
    failure_info: NotRequired["aws_sdk_sesv2.types.failure_info.FailureInfo"]
    """<p>The failure details about an import job.</p>"""
    job_status: NotRequired["aws_sdk_sesv2.types.job_status.JobStatus"]
    """<p>The status of the import job.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The time stamp of when the import job was created.</p>"""
    completed_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The time stamp of when the import job was completed.</p>"""
    processed_records_count: NotRequired[
        "aws_sdk_sesv2.types.processed_records_count.ProcessedRecordsCount"
    ]
    """<p>The current number of records processed.</p>"""
    failed_records_count: NotRequired[
        "aws_sdk_sesv2.types.failed_records_count.FailedRecordsCount"
    ]
    """<p>The number of records that failed processing because of invalid input or other reasons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "import_destination" in value:
        import aws_sdk_sesv2.types.import_destination

        out["ImportDestination"] = (
            aws_sdk_sesv2.types.import_destination.serialize_json(
                value["import_destination"]
            )
        )
    if "import_data_source" in value:
        import aws_sdk_sesv2.types.import_data_source

        out["ImportDataSource"] = aws_sdk_sesv2.types.import_data_source.serialize_json(
            value["import_data_source"]
        )
    if "failure_info" in value:
        import aws_sdk_sesv2.types.failure_info

        out["FailureInfo"] = aws_sdk_sesv2.types.failure_info.serialize_json(
            value["failure_info"]
        )
    if "job_status" in value:
        import aws_sdk_sesv2.types.job_status

        out["JobStatus"] = aws_sdk_sesv2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "created_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CreatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "completed_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CompletedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["completed_timestamp"]
        )
    if "processed_records_count" in value:
        out["ProcessedRecordsCount"] = value["processed_records_count"]
    if "failed_records_count" in value:
        out["FailedRecordsCount"] = value["failed_records_count"]
    return out


def deserialize_json(data: dict) -> GetImportJobResponse:
    out: GetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "ImportDestination" in data:
        import aws_sdk_sesv2.types.import_destination

        out["import_destination"] = (
            aws_sdk_sesv2.types.import_destination.deserialize_json(
                data["ImportDestination"]
            )
        )
    if "ImportDataSource" in data:
        import aws_sdk_sesv2.types.import_data_source

        out["import_data_source"] = (
            aws_sdk_sesv2.types.import_data_source.deserialize_json(
                data["ImportDataSource"]
            )
        )
    if "FailureInfo" in data:
        import aws_sdk_sesv2.types.failure_info

        out["failure_info"] = aws_sdk_sesv2.types.failure_info.deserialize_json(
            data["FailureInfo"]
        )
    if "JobStatus" in data:
        import aws_sdk_sesv2.types.job_status

        out["job_status"] = aws_sdk_sesv2.types.job_status.deserialize_json(
            data["JobStatus"]
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["created_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "CompletedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["completed_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CompletedTimestamp"]
        )
    if "ProcessedRecordsCount" in data:
        out["processed_records_count"] = data["ProcessedRecordsCount"]
    if "FailedRecordsCount" in data:
        out["failed_records_count"] = data["FailedRecordsCount"]
    return out
