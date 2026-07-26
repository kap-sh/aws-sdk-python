"""Generated from Smithy shape ``com.amazonaws.glue#IcebergCompactionMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dpu_counts
    import capo_glue.types.dpu_duration_in_hour
    import capo_glue.types.dpu_hours
    import capo_glue.types.metric_counts


class IcebergCompactionMetrics(TypedDict, closed=True):
    number_of_bytes_compacted: "capo_glue.types.metric_counts.metricCounts"
    """<p>The number of bytes removed by the compaction job run.</p>"""
    number_of_files_compacted: "capo_glue.types.metric_counts.metricCounts"
    """<p>The number of files removed by the compaction job run.</p>"""
    dpu_hours: "capo_glue.types.dpu_hours.dpuHours"
    """<p>The number of DPU hours consumed by the job.</p>"""
    number_of_dpus: "capo_glue.types.dpu_counts.dpuCounts"
    """<p>The number of DPUs consumed by the job, rounded up to the nearest whole number.</p>"""
    job_duration_in_hour: "capo_glue.types.dpu_duration_in_hour.dpuDurationInHour"
    """<p>The duration of the job in hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergCompactionMetrics) -> dict:
    out: dict = {}
    out["NumberOfBytesCompacted"] = value.get("number_of_bytes_compacted", 0)
    out["NumberOfFilesCompacted"] = value.get("number_of_files_compacted", 0)
    out["DpuHours"] = value.get("dpu_hours", 0)
    out["NumberOfDpus"] = value.get("number_of_dpus", 0)
    out["JobDurationInHour"] = value.get("job_duration_in_hour", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergCompactionMetrics:
    out: IcebergCompactionMetrics = {}  # type: ignore[typeddict-item]
    if "NumberOfBytesCompacted" in data:
        out["number_of_bytes_compacted"] = data["NumberOfBytesCompacted"]
    else:
        out["number_of_bytes_compacted"] = 0
    if "NumberOfFilesCompacted" in data:
        out["number_of_files_compacted"] = data["NumberOfFilesCompacted"]
    else:
        out["number_of_files_compacted"] = 0
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
