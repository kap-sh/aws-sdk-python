"""Generated from Smithy shape ``com.amazonaws.pinpoint#ExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.export_job_resource
    import aws_sdk_pinpoint.types.job_status
    import aws_sdk_pinpoint.types.list_of__string


class ExportJobResponse(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that's associated with the export job.</p>"""
    completed_pieces: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The number of pieces that were processed successfully (completed) by the export job, as of the time of the request.</p>"""
    completion_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the export job was completed.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the export job was created.</p>"""
    definition: NotRequired[
        "aws_sdk_pinpoint.types.export_job_resource.ExportJobResource"
    ]
    """<p>The resource settings that apply to the export job.</p>"""
    failed_pieces: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The number of pieces that weren't processed successfully (failed) by the export job, as of the time of the request.</p>"""
    failures: NotRequired["aws_sdk_pinpoint.types.list_of__string.ListOf__string"]
    """<p>An array of entries, one for each of the first 100 entries that weren't processed successfully (failed) by the export job, if any.</p>"""
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the export job.</p>"""
    job_status: NotRequired["aws_sdk_pinpoint.types.job_status.JobStatus"]
    """<p>The status of the export job. The job status is FAILED if Amazon Pinpoint wasn't able to process one or more pieces in the job.</p>"""
    total_failures: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The total number of endpoint definitions that weren't processed successfully (failed) by the export job, typically because an error, such as a syntax error, occurred.</p>"""
    total_pieces: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The total number of pieces that must be processed to complete the export job. Each piece consists of an approximately equal portion of the endpoint definitions that are part of the export job.</p>"""
    total_processed: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The total number of endpoint definitions that were processed by the export job.</p>"""
    type: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The job type. This value is EXPORT for export jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "completed_pieces" in value:
        out["CompletedPieces"] = value["completed_pieces"]
    if "completion_date" in value:
        out["CompletionDate"] = value["completion_date"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "definition" in value:
        import aws_sdk_pinpoint.types.export_job_resource

        out["Definition"] = aws_sdk_pinpoint.types.export_job_resource.serialize_json(
            value["definition"]
        )
    if "failed_pieces" in value:
        out["FailedPieces"] = value["failed_pieces"]
    if "failures" in value:
        import aws_sdk_pinpoint.types.list_of__string

        out["Failures"] = aws_sdk_pinpoint.types.list_of__string.serialize_json(
            value["failures"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "job_status" in value:
        import aws_sdk_pinpoint.types.job_status

        out["JobStatus"] = aws_sdk_pinpoint.types.job_status.serialize_json(
            value["job_status"]
        )
    if "total_failures" in value:
        out["TotalFailures"] = value["total_failures"]
    if "total_pieces" in value:
        out["TotalPieces"] = value["total_pieces"]
    if "total_processed" in value:
        out["TotalProcessed"] = value["total_processed"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ExportJobResponse:
    out: ExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "CompletedPieces" in data:
        out["completed_pieces"] = data["CompletedPieces"]
    if "CompletionDate" in data:
        out["completion_date"] = data["CompletionDate"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "Definition" in data:
        import aws_sdk_pinpoint.types.export_job_resource

        out["definition"] = aws_sdk_pinpoint.types.export_job_resource.deserialize_json(
            data["Definition"]
        )
    if "FailedPieces" in data:
        out["failed_pieces"] = data["FailedPieces"]
    if "Failures" in data:
        import aws_sdk_pinpoint.types.list_of__string

        out["failures"] = aws_sdk_pinpoint.types.list_of__string.deserialize_json(
            data["Failures"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "JobStatus" in data:
        import aws_sdk_pinpoint.types.job_status

        out["job_status"] = aws_sdk_pinpoint.types.job_status.deserialize_json(
            data["JobStatus"]
        )
    if "TotalFailures" in data:
        out["total_failures"] = data["TotalFailures"]
    if "TotalPieces" in data:
        out["total_pieces"] = data["TotalPieces"]
    if "TotalProcessed" in data:
        out["total_processed"] = data["TotalProcessed"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
