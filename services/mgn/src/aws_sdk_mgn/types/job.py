"""Generated from Smithy shape ``com.amazonaws.mgn#Job``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.initiated_by
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.job_id
    import aws_sdk_mgn.types.job_status
    import aws_sdk_mgn.types.job_type
    import aws_sdk_mgn.types.participating_servers
    import aws_sdk_mgn.types.tags_map


class Job(TypedDict):
    job_id: "aws_sdk_mgn.types.job_id.JobID"
    """<p>Job ID.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>the ARN of the specific Job.</p>"""
    type: NotRequired["aws_sdk_mgn.types.job_type.JobType"]
    """<p>Job type.</p>"""
    initiated_by: NotRequired["aws_sdk_mgn.types.initiated_by.InitiatedBy"]
    """<p>Job initiated by field.</p>"""
    creation_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Job creation time.</p>"""
    end_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Job end time.</p>"""
    status: NotRequired["aws_sdk_mgn.types.job_status.JobStatus"]
    """<p>Job status.</p>"""
    participating_servers: NotRequired[
        "aws_sdk_mgn.types.participating_servers.ParticipatingServers"
    ]
    """<p>Servers participating in a specific Job.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Tags associated with specific Job.</p>"""


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
        import aws_sdk_mgn.types.participating_servers

        out["participatingServers"] = (
            aws_sdk_mgn.types.participating_servers.serialize_json(
                value["participating_servers"]
            )
        )
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
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
        import aws_sdk_mgn.types.participating_servers

        out["participating_servers"] = (
            aws_sdk_mgn.types.participating_servers.deserialize_json(
                data["participatingServers"]
            )
        )
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    return out
