"""Generated from Smithy shape ``com.amazonaws.mgn#ExportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.arn
    import capo_mgn.types.export_id
    import capo_mgn.types.export_status
    import capo_mgn.types.export_task_summary
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_key
    import capo_mgn.types.tags_map


class ExportTask(TypedDict, closed=True):
    export_id: NotRequired["capo_mgn.types.export_id.ExportID"]
    """<p>Export task id.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>ExportTask arn.</p>"""
    s3_bucket: NotRequired["capo_mgn.types.s3_bucket_name.S3BucketName"]
    """<p>Export task s3 bucket.</p>"""
    s3_key: NotRequired["capo_mgn.types.s3_key.S3Key"]
    """<p>Export task s3 key.</p>"""
    s3_bucket_owner: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Export task s3 bucket owner.</p>"""
    creation_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Export task creation datetime.</p>"""
    end_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Export task end datetime.</p>"""
    status: NotRequired["capo_mgn.types.export_status.ExportStatus"]
    """<p>Export task status.</p>"""
    progress_percentage: NotRequired["float"]
    """<p>Export task progress percentage.</p>"""
    summary: NotRequired["capo_mgn.types.export_task_summary.ExportTaskSummary"]
    """<p>Export task summary.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Export task tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTask) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportID"] = value["export_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["s3Key"] = value["s3_key"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "end_date_time" in value:
        out["endDateTime"] = value["end_date_time"]
    if "status" in value:
        out["status"] = value["status"]
    if "progress_percentage" in value:
        out["progressPercentage"] = value["progress_percentage"]
    if "summary" in value:
        import capo_mgn.types.export_task_summary

        out["summary"] = capo_mgn.types.export_task_summary.serialize_json(
            value["summary"]
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    if "exportID" in data:
        out["export_id"] = data["exportID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3Key" in data:
        out["s3_key"] = data["s3Key"]
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if "creationDateTime" in data:
        out["creation_date_time"] = data["creationDateTime"]
    if "endDateTime" in data:
        out["end_date_time"] = data["endDateTime"]
    if "status" in data:
        out["status"] = data["status"]
    if "progressPercentage" in data:
        out["progress_percentage"] = data["progressPercentage"]
    if "summary" in data:
        import capo_mgn.types.export_task_summary

        out["summary"] = capo_mgn.types.export_task_summary.deserialize_json(
            data["summary"]
        )
    if "tags" in data:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out
