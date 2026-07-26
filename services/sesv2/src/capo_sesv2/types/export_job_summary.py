"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.export_source_type
    import capo_sesv2.types.job_id
    import capo_sesv2.types.job_status
    import capo_sesv2.types.timestamp


class ExportJobSummary(TypedDict, closed=True):
    job_id: NotRequired["capo_sesv2.types.job_id.JobId"]
    """<p>The export job ID.</p>"""
    export_source_type: NotRequired[
        "capo_sesv2.types.export_source_type.ExportSourceType"
    ]
    """<p>The source type of the export job.</p>"""
    job_status: NotRequired["capo_sesv2.types.job_status.JobStatus"]
    """<p>The status of the export job.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of when the export job was created.</p>"""
    completed_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of when the export job was completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobSummary) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "export_source_type" in value:
        import capo_sesv2.types.export_source_type

        out["ExportSourceType"] = capo_sesv2.types.export_source_type.serialize_json(
            value["export_source_type"]
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
    if "completed_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CompletedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["completed_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ExportJobSummary:
    out: ExportJobSummary = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "ExportSourceType" in data:
        import capo_sesv2.types.export_source_type

        out["export_source_type"] = (
            capo_sesv2.types.export_source_type.deserialize_json(
                data["ExportSourceType"]
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
    if "CompletedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["completed_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CompletedTimestamp"]
        )
    return out
