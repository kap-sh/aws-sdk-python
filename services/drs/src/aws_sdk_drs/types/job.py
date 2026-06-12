"""Generated from Smithy shape ``com.amazonaws.drs#Job``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_drs.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.initiated_by
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.job_id
    import aws_sdk_drs.types.job_status
    import aws_sdk_drs.types.job_type
    import aws_sdk_drs.types.participating_resources
    import aws_sdk_drs.types.participating_servers
    import aws_sdk_drs.types.tags_map

class Job(TypedDict):
    job_id: "aws_sdk_drs.types.job_id.JobID"
    """<p>The ID of the Job.</p>"""
    arn: NotRequired["aws_sdk_drs.types.arn.ARN"]
    """<p>The ARN of a Job.</p>"""
    type: NotRequired["aws_sdk_drs.types.job_type.JobType"]
    """<p>The type of the Job.</p>"""
    initiated_by: NotRequired["aws_sdk_drs.types.initiated_by.InitiatedBy"]
    """<p>A string representing who initiated the Job.</p>"""
    creation_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time of when the Job was created.</p>"""
    end_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time of when the Job ended.</p>"""
    status: NotRequired["aws_sdk_drs.types.job_status.JobStatus"]
    """<p>The status of the Job.</p>"""
    participating_servers: NotRequired["aws_sdk_drs.types.participating_servers.ParticipatingServers"]
    """<p>A list of servers that the Job is acting upon.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the Job.</p>"""
    participating_resources: NotRequired["aws_sdk_drs.types.participating_resources.ParticipatingResources"]
    """<p>A list of resources that the Job is acting upon.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        out["type"] = value["type"]
    if "initiated_by" in value:
        out["initiatedBy"] = value["initiated_by"]
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "end_date_time" in value:
        out["endDateTime"] = value["end_date_time"]
    if "status" in value:
        out["status"] = value["status"]
    if "participating_servers" in value:
        import aws_sdk_drs.types.participating_servers
        out["participatingServers"] = aws_sdk_drs.types.participating_servers.serialize_json(value["participating_servers"])
    if "tags" in value:
        import aws_sdk_drs.types.tags_map
        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    if "participating_resources" in value:
        import aws_sdk_drs.types.participating_resources
        out["participatingResources"] = aws_sdk_drs.types.participating_resources.serialize_json(value["participating_resources"])
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    else:
        raise DeserializationError("Job.job_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        out["type"] = data["type"]
    if "initiatedBy" in data:
        out["initiated_by"] = data["initiatedBy"]
    if "creationDateTime" in data:
        out["creation_date_time"] = data["creationDateTime"]
    if "endDateTime" in data:
        out["end_date_time"] = data["endDateTime"]
    if "status" in data:
        out["status"] = data["status"]
    if "participatingServers" in data:
        import aws_sdk_drs.types.participating_servers
        out["participating_servers"] = aws_sdk_drs.types.participating_servers.deserialize_json(data["participatingServers"])
    if "tags" in data:
        import aws_sdk_drs.types.tags_map
        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    if "participatingResources" in data:
        import aws_sdk_drs.types.participating_resources
        out["participating_resources"] = aws_sdk_drs.types.participating_resources.deserialize_json(data["participatingResources"])
    return out