"""Generated from Smithy shape ``com.amazonaws.glue#RunMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class RunMetrics(TypedDict):
    number_of_bytes_compacted: NotRequired[
        "aws_sdk_glue.types.message_string.MessageString"
    ]
    """<p>The number of bytes removed by the compaction job run.</p>"""
    number_of_files_compacted: NotRequired[
        "aws_sdk_glue.types.message_string.MessageString"
    ]
    """<p>The number of files removed by the compaction job run.</p>"""
    number_of_dpus: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>The number of DPUs consumed by the job, rounded up to the nearest whole number.</p>"""
    job_duration_in_hour: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>The duration of the job in hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunMetrics) -> dict:
    out: dict = {}
    if "number_of_bytes_compacted" in value:
        out["NumberOfBytesCompacted"] = value["number_of_bytes_compacted"]
    if "number_of_files_compacted" in value:
        out["NumberOfFilesCompacted"] = value["number_of_files_compacted"]
    if "number_of_dpus" in value:
        out["NumberOfDpus"] = value["number_of_dpus"]
    if "job_duration_in_hour" in value:
        out["JobDurationInHour"] = value["job_duration_in_hour"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RunMetrics:
    out: RunMetrics = {}  # type: ignore[typeddict-item]
    if "NumberOfBytesCompacted" in data:
        out["number_of_bytes_compacted"] = data["NumberOfBytesCompacted"]
    if "NumberOfFilesCompacted" in data:
        out["number_of_files_compacted"] = data["NumberOfFilesCompacted"]
    if "NumberOfDpus" in data:
        out["number_of_dpus"] = data["NumberOfDpus"]
    if "JobDurationInHour" in data:
        out["job_duration_in_hour"] = data["JobDurationInHour"]
    return out
