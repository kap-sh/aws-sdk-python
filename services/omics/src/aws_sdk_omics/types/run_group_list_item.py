"""Generated from Smithy shape ``com.amazonaws.omics#RunGroupListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_arn
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.run_group_name
    import aws_sdk_omics.types.run_group_timestamp


class RunGroupListItem(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_omics.types.run_group_arn.RunGroupArn"]
    """<p>The group's ARN.</p>"""
    id: NotRequired["aws_sdk_omics.types.run_group_id.RunGroupId"]
    """<p>The group's ID.</p>"""
    name: NotRequired["aws_sdk_omics.types.run_group_name.RunGroupName"]
    """<p>The group's name.</p>"""
    max_cpus: NotRequired["int"]
    """<p>The group's maximum CPU count setting.</p>"""
    max_runs: NotRequired["int"]
    """<p>The group's maximum concurrent run setting.</p>"""
    max_duration: NotRequired["int"]
    """<p>The group's maximum duration setting in minutes.</p>"""
    creation_time: NotRequired[
        "aws_sdk_omics.types.run_group_timestamp.RunGroupTimestamp"
    ]
    """<p>When the group was created.</p>"""
    max_gpus: NotRequired["int"]
    """<p> The maximum GPUs that can be used by a run group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunGroupListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "max_cpus" in value:
        out["maxCpus"] = value["max_cpus"]
    if "max_runs" in value:
        out["maxRuns"] = value["max_runs"]
    if "max_duration" in value:
        out["maxDuration"] = value["max_duration"]
    if "creation_time" in value:
        import aws_sdk_omics.types.run_group_timestamp

        out["creationTime"] = aws_sdk_omics.types.run_group_timestamp.serialize_json(
            value["creation_time"]
        )
    if "max_gpus" in value:
        out["maxGpus"] = value["max_gpus"]
    return out


def deserialize_json(data: dict) -> RunGroupListItem:
    out: RunGroupListItem = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "maxCpus" in data:
        out["max_cpus"] = data["maxCpus"]
    if "maxRuns" in data:
        out["max_runs"] = data["maxRuns"]
    if "maxDuration" in data:
        out["max_duration"] = data["maxDuration"]
    if "creationTime" in data:
        import aws_sdk_omics.types.run_group_timestamp

        out["creation_time"] = aws_sdk_omics.types.run_group_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "maxGpus" in data:
        out["max_gpus"] = data["maxGpus"]
    return out
