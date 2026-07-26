"""Generated from Smithy shape ``com.amazonaws.braket#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.job_arn
    import capo_braket.types.job_primary_status
    import capo_braket.types.string256
    import capo_braket.types.tags_map


class JobSummary(TypedDict, closed=True):
    status: "capo_braket.types.job_primary_status.JobPrimaryStatus"
    """<p>The status of the Amazon Braket hybrid job.</p>"""
    job_arn: "capo_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    device: "capo_braket.types.string256.String256"
    """<p>The primary device used by an Amazon Braket hybrid job.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the Amazon Braket hybrid job was created.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job was started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job ended.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>Displays the key, value pairs of tags associated with this hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    out["device"] = value["device"]
    import capo_braket.types._prelude.timestamp

    out["createdAt"] = capo_braket.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "started_at" in value:
        import capo_braket.types._prelude.timestamp

        out["startedAt"] = capo_braket.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_braket.types._prelude.timestamp

        out["endedAt"] = capo_braket.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("JobSummary.status required")
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("JobSummary.job_arn required")
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("JobSummary.job_name required")
    if "device" in data:
        out["device"] = data["device"]
    else:
        raise DeserializationError("JobSummary.device required")
    if "createdAt" in data:
        import capo_braket.types._prelude.timestamp

        out["created_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("JobSummary.created_at required")
    if "startedAt" in data:
        import capo_braket.types._prelude.timestamp

        out["started_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import capo_braket.types._prelude.timestamp

        out["ended_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "tags" in data:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    return out
