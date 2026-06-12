"""Generated from Smithy shape ``com.amazonaws.glue#IcebergOrphanFileDeletionMetrics``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.dpu_counts
    import aws_sdk_glue.types.dpu_duration_in_hour
    import aws_sdk_glue.types.dpu_hours
    import aws_sdk_glue.types.metric_counts


class IcebergOrphanFileDeletionMetrics(TypedDict):
    number_of_orphan_files_deleted: "aws_sdk_glue.types.metric_counts.metricCounts"
    """<p>The number of orphan files deleted by the orphan file deletion job run.</p>"""
    dpu_hours: "aws_sdk_glue.types.dpu_hours.dpuHours"
    """<p>The number of DPU hours consumed by the job.</p>"""
    number_of_dpus: "aws_sdk_glue.types.dpu_counts.dpuCounts"
    """<p>The number of DPUs consumed by the job, rounded up to the nearest whole number.</p>"""
    job_duration_in_hour: "aws_sdk_glue.types.dpu_duration_in_hour.dpuDurationInHour"
    """<p>The duration of the job in hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergOrphanFileDeletionMetrics) -> dict:
    out: dict = {}
    out["NumberOfOrphanFilesDeleted"] = value.get("number_of_orphan_files_deleted", 0)
    out["DpuHours"] = value.get("dpu_hours", 0)
    out["NumberOfDpus"] = value.get("number_of_dpus", 0)
    out["JobDurationInHour"] = value.get("job_duration_in_hour", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergOrphanFileDeletionMetrics:
    out: IcebergOrphanFileDeletionMetrics = {}  # type: ignore[typeddict-item]
    if "NumberOfOrphanFilesDeleted" in data:
        out["number_of_orphan_files_deleted"] = data["NumberOfOrphanFilesDeleted"]
    else:
        out["number_of_orphan_files_deleted"] = 0
    if "DpuHours" in data:
        out["dpu_hours"] = data["DpuHours"]
    else:
        out["dpu_hours"] = 0
    if "NumberOfDpus" in data:
        out["number_of_dpus"] = data["NumberOfDpus"]
    else:
        out["number_of_dpus"] = 0
    if "JobDurationInHour" in data:
        out["job_duration_in_hour"] = data["JobDurationInHour"]
    else:
        out["job_duration_in_hour"] = 0
    return out
