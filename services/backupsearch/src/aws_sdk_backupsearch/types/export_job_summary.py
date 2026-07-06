"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backupsearch.types.export_job_arn
    import aws_sdk_backupsearch.types.export_job_status
    import aws_sdk_backupsearch.types.generic_id
    import aws_sdk_backupsearch.types.search_job_arn


class ExportJobSummary(TypedDict, closed=True):
    export_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId"
    """<p>This is the unique string that identifies a specific export job.</p>"""
    export_job_arn: NotRequired[
        "aws_sdk_backupsearch.types.export_job_arn.ExportJobArn"
    ]
    """<p>This is the unique ARN (Amazon Resource Name) that belongs to the new export job.</p>"""
    status: NotRequired["aws_sdk_backupsearch.types.export_job_status.ExportJobStatus"]
    """<p>The status of the export job is one of the following:</p> <p> <code>CREATED</code>; <code>RUNNING</code>; <code>FAILED</code>; or <code>COMPLETED</code>.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>This is a timestamp of the time the export job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>This is a timestamp of the time the export job compeleted.</p>"""
    status_message: NotRequired["str"]
    """<p>A status message is a string that is returned for an export job.</p> <p>A status message is included for any status other than <code>COMPLETED</code> without issues.</p>"""
    search_job_arn: NotRequired[
        "aws_sdk_backupsearch.types.search_job_arn.SearchJobArn"
    ]
    """<p>The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobSummary) -> dict:
    out: dict = {}
    out["ExportJobIdentifier"] = value["export_job_identifier"]
    if "export_job_arn" in value:
        out["ExportJobArn"] = value["export_job_arn"]
    if "status" in value:
        import aws_sdk_backupsearch.types.export_job_status

        out["Status"] = aws_sdk_backupsearch.types.export_job_status.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CreationTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "completion_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CompletionTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["completion_time"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "search_job_arn" in value:
        out["SearchJobArn"] = value["search_job_arn"]
    return out


def deserialize_json(data: dict) -> ExportJobSummary:
    out: ExportJobSummary = {}  # type: ignore[typeddict-item]
    if "ExportJobIdentifier" in data:
        out["export_job_identifier"] = data["ExportJobIdentifier"]
    else:
        raise DeserializationError("ExportJobSummary.export_job_identifier required")
    if "ExportJobArn" in data:
        out["export_job_arn"] = data["ExportJobArn"]
    if "Status" in data:
        import aws_sdk_backupsearch.types.export_job_status

        out["status"] = aws_sdk_backupsearch.types.export_job_status.deserialize_json(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CompletionTime"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "SearchJobArn" in data:
        out["search_job_arn"] = data["SearchJobArn"]
    return out
