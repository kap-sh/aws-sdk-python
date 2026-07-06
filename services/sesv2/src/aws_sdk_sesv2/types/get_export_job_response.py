"""Generated from Smithy shape ``com.amazonaws.sesv2#GetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.export_data_source
    import aws_sdk_sesv2.types.export_destination
    import aws_sdk_sesv2.types.export_source_type
    import aws_sdk_sesv2.types.export_statistics
    import aws_sdk_sesv2.types.failure_info
    import aws_sdk_sesv2.types.job_id
    import aws_sdk_sesv2.types.job_status
    import aws_sdk_sesv2.types.timestamp


class GetExportJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_sesv2.types.job_id.JobId"]
    """<p>The export job ID.</p>"""
    export_source_type: NotRequired[
        "aws_sdk_sesv2.types.export_source_type.ExportSourceType"
    ]
    """<p>The type of source of the export job.</p>"""
    job_status: NotRequired["aws_sdk_sesv2.types.job_status.JobStatus"]
    """<p>The status of the export job.</p>"""
    export_destination: NotRequired[
        "aws_sdk_sesv2.types.export_destination.ExportDestination"
    ]
    """<p>The destination of the export job.</p>"""
    export_data_source: NotRequired[
        "aws_sdk_sesv2.types.export_data_source.ExportDataSource"
    ]
    """<p>The data source of the export job.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of when the export job was created.</p>"""
    completed_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of when the export job was completed.</p>"""
    failure_info: NotRequired["aws_sdk_sesv2.types.failure_info.FailureInfo"]
    """<p>The failure details about an export job.</p>"""
    statistics: NotRequired["aws_sdk_sesv2.types.export_statistics.ExportStatistics"]
    """<p>The statistics about the export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "export_source_type" in value:
        import aws_sdk_sesv2.types.export_source_type

        out["ExportSourceType"] = aws_sdk_sesv2.types.export_source_type.serialize_json(
            value["export_source_type"]
        )
    if "job_status" in value:
        import aws_sdk_sesv2.types.job_status

        out["JobStatus"] = aws_sdk_sesv2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "export_destination" in value:
        import aws_sdk_sesv2.types.export_destination

        out["ExportDestination"] = (
            aws_sdk_sesv2.types.export_destination.serialize_json(
                value["export_destination"]
            )
        )
    if "export_data_source" in value:
        import aws_sdk_sesv2.types.export_data_source

        out["ExportDataSource"] = aws_sdk_sesv2.types.export_data_source.serialize_json(
            value["export_data_source"]
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
    if "failure_info" in value:
        import aws_sdk_sesv2.types.failure_info

        out["FailureInfo"] = aws_sdk_sesv2.types.failure_info.serialize_json(
            value["failure_info"]
        )
    if "statistics" in value:
        import aws_sdk_sesv2.types.export_statistics

        out["Statistics"] = aws_sdk_sesv2.types.export_statistics.serialize_json(
            value["statistics"]
        )
    return out


def deserialize_json(data: dict) -> GetExportJobResponse:
    out: GetExportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "ExportSourceType" in data:
        import aws_sdk_sesv2.types.export_source_type

        out["export_source_type"] = (
            aws_sdk_sesv2.types.export_source_type.deserialize_json(
                data["ExportSourceType"]
            )
        )
    if "JobStatus" in data:
        import aws_sdk_sesv2.types.job_status

        out["job_status"] = aws_sdk_sesv2.types.job_status.deserialize_json(
            data["JobStatus"]
        )
    if "ExportDestination" in data:
        import aws_sdk_sesv2.types.export_destination

        out["export_destination"] = (
            aws_sdk_sesv2.types.export_destination.deserialize_json(
                data["ExportDestination"]
            )
        )
    if "ExportDataSource" in data:
        import aws_sdk_sesv2.types.export_data_source

        out["export_data_source"] = (
            aws_sdk_sesv2.types.export_data_source.deserialize_json(
                data["ExportDataSource"]
            )
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
    if "FailureInfo" in data:
        import aws_sdk_sesv2.types.failure_info

        out["failure_info"] = aws_sdk_sesv2.types.failure_info.deserialize_json(
            data["FailureInfo"]
        )
    if "Statistics" in data:
        import aws_sdk_sesv2.types.export_statistics

        out["statistics"] = aws_sdk_sesv2.types.export_statistics.deserialize_json(
            data["Statistics"]
        )
    return out
