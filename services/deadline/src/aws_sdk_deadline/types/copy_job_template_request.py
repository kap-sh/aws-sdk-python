"""Generated from Smithy shape ``com.amazonaws.deadline#CopyJobTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.s3_location


class CopyJobTemplateRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to copy.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID to copy.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID to copy.</p>"""
    target_s3_location: "aws_sdk_deadline.types.s3_location.S3Location"
    """<p>The Amazon S3 bucket name and key where you would like to add a copy of the job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobTemplateRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.s3_location

    out["targetS3Location"] = aws_sdk_deadline.types.s3_location.serialize_json(
        value["target_s3_location"]
    )
    return out


def deserialize_json(data: dict) -> CopyJobTemplateRequest:
    out: CopyJobTemplateRequest = {}  # type: ignore[typeddict-item]
    if "targetS3Location" in data:
        import aws_sdk_deadline.types.s3_location

        out["target_s3_location"] = aws_sdk_deadline.types.s3_location.deserialize_json(
            data["targetS3Location"]
        )
    else:
        raise DeserializationError("CopyJobTemplateRequest.target_s3_location required")
    return out
