"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.failed_records_count
    import capo_sesv2.types.import_destination
    import capo_sesv2.types.job_id
    import capo_sesv2.types.job_status
    import capo_sesv2.types.processed_records_count
    import capo_sesv2.types.timestamp


class ImportJobSummary(TypedDict, closed=True):
    job_id: NotRequired["capo_sesv2.types.job_id.JobId"]
    import_destination: NotRequired[
        "capo_sesv2.types.import_destination.ImportDestination"
    ]
    job_status: NotRequired["capo_sesv2.types.job_status.JobStatus"]
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the import job was created.</p>"""
    processed_records_count: NotRequired[
        "capo_sesv2.types.processed_records_count.ProcessedRecordsCount"
    ]
    """<p>The current number of records processed.</p>"""
    failed_records_count: NotRequired[
        "capo_sesv2.types.failed_records_count.FailedRecordsCount"
    ]
    """<p>The number of records that failed processing because of invalid input or other reasons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobSummary) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "import_destination" in value:
        import capo_sesv2.types.import_destination

        out["ImportDestination"] = capo_sesv2.types.import_destination.serialize_json(
            value["import_destination"]
        )
    if "job_status" in value:
        import capo_sesv2.types.job_status

        out["JobStatus"] = capo_sesv2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "created_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CreatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "processed_records_count" in value:
        out["ProcessedRecordsCount"] = value["processed_records_count"]
    if "failed_records_count" in value:
        out["FailedRecordsCount"] = value["failed_records_count"]
    return out


def deserialize_json(data: dict) -> ImportJobSummary:
    out: ImportJobSummary = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "ImportDestination" in data:
        import capo_sesv2.types.import_destination

        out["import_destination"] = (
            capo_sesv2.types.import_destination.deserialize_json(
                data["ImportDestination"]
            )
        )
    if "JobStatus" in data:
        import capo_sesv2.types.job_status

        out["job_status"] = capo_sesv2.types.job_status.deserialize_json(
            data["JobStatus"]
        )
    if "CreatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["created_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "ProcessedRecordsCount" in data:
        out["processed_records_count"] = data["ProcessedRecordsCount"]
    if "FailedRecordsCount" in data:
        out["failed_records_count"] = data["FailedRecordsCount"]
    return out
