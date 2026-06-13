"""Generated from Smithy shape ``com.amazonaws.omics#CreateRunGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_name
    import aws_sdk_omics.types.run_group_request_id
    import aws_sdk_omics.types.tag_map


class CreateRunGroupRequest(TypedDict):
    name: NotRequired["aws_sdk_omics.types.run_group_name.RunGroupName"]
    """<p>A name for the group.</p>"""
    max_cpus: NotRequired["int"]
    """<p>The maximum number of CPUs that can run concurrently across all active runs in the run group.</p>"""
    max_runs: NotRequired["int"]
    """<p>The maximum number of runs that can be running at the same time.</p>"""
    max_duration: NotRequired["int"]
    """<p>The maximum time for each run (in minutes). If a run exceeds the maximum run time, the run fails automatically.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the group.</p>"""
    request_id: "aws_sdk_omics.types.run_group_request_id.RunGroupRequestId"
    """<p>To ensure that requests don't run multiple times, specify a unique ID for each request.</p>"""
    max_gpus: NotRequired["int"]
    """<p>The maximum number of GPUs that can run concurrently across all active runs in the run group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRunGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "max_cpus" in value:
        out["maxCpus"] = value["max_cpus"]
    if "max_runs" in value:
        out["maxRuns"] = value["max_runs"]
    if "max_duration" in value:
        out["maxDuration"] = value["max_duration"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    if "max_gpus" in value:
        out["maxGpus"] = value["max_gpus"]
    return out


def deserialize_json(data: dict) -> CreateRunGroupRequest:
    out: CreateRunGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "maxCpus" in data:
        out["max_cpus"] = data["maxCpus"]
    if "maxRuns" in data:
        out["max_runs"] = data["maxRuns"]
    if "maxDuration" in data:
        out["max_duration"] = data["maxDuration"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("CreateRunGroupRequest.request_id required")
    if "maxGpus" in data:
        out["max_gpus"] = data["maxGpus"]
    return out
