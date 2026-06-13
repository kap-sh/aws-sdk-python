"""Generated from Smithy shape ``com.amazonaws.omics#UpdateRunGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.run_group_name


class UpdateRunGroupRequest(TypedDict):
    id: "aws_sdk_omics.types.run_group_id.RunGroupId"
    """<p>The group's ID.</p>"""
    name: NotRequired["aws_sdk_omics.types.run_group_name.RunGroupName"]
    """<p>A name for the group.</p>"""
    max_cpus: NotRequired["int"]
    """<p>The maximum number of CPUs to use.</p>"""
    max_runs: NotRequired["int"]
    """<p>The maximum number of concurrent runs for the group.</p>"""
    max_duration: NotRequired["int"]
    """<p>A maximum run time for the group in minutes.</p>"""
    max_gpus: NotRequired["int"]
    """<p>The maximum GPUs that can be used by a run group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRunGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "max_cpus" in value:
        out["maxCpus"] = value["max_cpus"]
    if "max_runs" in value:
        out["maxRuns"] = value["max_runs"]
    if "max_duration" in value:
        out["maxDuration"] = value["max_duration"]
    if "max_gpus" in value:
        out["maxGpus"] = value["max_gpus"]
    return out


def deserialize_json(data: dict) -> UpdateRunGroupRequest:
    out: UpdateRunGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "maxCpus" in data:
        out["max_cpus"] = data["maxCpus"]
    if "maxRuns" in data:
        out["max_runs"] = data["maxRuns"]
    if "maxDuration" in data:
        out["max_duration"] = data["maxDuration"]
    if "maxGpus" in data:
        out["max_gpus"] = data["maxGpus"]
    return out
