"""Generated from Smithy shape ``com.amazonaws.braket#JobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_braket.types.job_arn
    import aws_sdk_braket.types.job_primary_status
    import aws_sdk_braket.types.string256
    import aws_sdk_braket.types.tags_map


class JobSummary(TypedDict):
    status: "aws_sdk_braket.types.job_primary_status.JobPrimaryStatus"
    """<p>The status of the Amazon Braket hybrid job.</p>"""
    job_arn: "aws_sdk_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    device: "aws_sdk_braket.types.string256.String256"
    """<p>The primary device used by an Amazon Braket hybrid job.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the Amazon Braket hybrid job was created.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job was started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job ended.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>Displays the key, value pairs of tags associated with this hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    out["device"] = value["device"]
    import aws_sdk_braket.types._prelude.timestamp

    out["createdAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "started_at" in value:
        import aws_sdk_braket.types._prelude.timestamp

        out["startedAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_braket.types._prelude.timestamp

        out["endedAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "tags" in value:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
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
        import aws_sdk_braket.types._prelude.timestamp

        out["created_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("JobSummary.created_at required")
    if "startedAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["started_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["ended_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "tags" in data:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    return out
