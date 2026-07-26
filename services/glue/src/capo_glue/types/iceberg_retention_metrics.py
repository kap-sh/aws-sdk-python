"""Generated from Smithy shape ``com.amazonaws.glue#IcebergRetentionMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dpu_counts
    import capo_glue.types.dpu_duration_in_hour
    import capo_glue.types.dpu_hours
    import capo_glue.types.metric_counts


class IcebergRetentionMetrics(TypedDict, closed=True):
    number_of_data_files_deleted: "capo_glue.types.metric_counts.metricCounts"
    """<p>The number of data files deleted by the retention job run.</p>"""
    number_of_manifest_files_deleted: "capo_glue.types.metric_counts.metricCounts"
    """<p>The number of manifest files deleted by the retention job run.</p>"""
    number_of_manifest_lists_deleted: "capo_glue.types.metric_counts.metricCounts"
    """<p>The number of manifest lists deleted by the retention job run.</p>"""
    dpu_hours: "capo_glue.types.dpu_hours.dpuHours"
    """<p>The number of DPU hours consumed by the job.</p>"""
    number_of_dpus: "capo_glue.types.dpu_counts.dpuCounts"
    """<p>The number of DPUs consumed by the job, rounded up to the nearest whole number.</p>"""
    job_duration_in_hour: "capo_glue.types.dpu_duration_in_hour.dpuDurationInHour"
    """<p>The duration of the job in hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergRetentionMetrics) -> dict:
    out: dict = {}
    out["NumberOfDataFilesDeleted"] = value.get("number_of_data_files_deleted", 0)
    out["NumberOfManifestFilesDeleted"] = value.get(
        "number_of_manifest_files_deleted", 0
    )
    out["NumberOfManifestListsDeleted"] = value.get(
        "number_of_manifest_lists_deleted", 0
    )
    out["DpuHours"] = value.get("dpu_hours", 0)
    out["NumberOfDpus"] = value.get("number_of_dpus", 0)
    out["JobDurationInHour"] = value.get("job_duration_in_hour", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergRetentionMetrics:
    out: IcebergRetentionMetrics = {}  # type: ignore[typeddict-item]
    if "NumberOfDataFilesDeleted" in data:
        out["number_of_data_files_deleted"] = data["NumberOfDataFilesDeleted"]
    else:
        out["number_of_data_files_deleted"] = 0
    if "NumberOfManifestFilesDeleted" in data:
        out["number_of_manifest_files_deleted"] = data["NumberOfManifestFilesDeleted"]
    else:
        out["number_of_manifest_files_deleted"] = 0
    if "NumberOfManifestListsDeleted" in data:
        out["number_of_manifest_lists_deleted"] = data["NumberOfManifestListsDeleted"]
    else:
        out["number_of_manifest_lists_deleted"] = 0
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
