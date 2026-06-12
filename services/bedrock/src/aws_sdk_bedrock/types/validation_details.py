"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.job_status_details
    import aws_sdk_bedrock.types.timestamp


class ValidationDetails(TypedDict):
    status: NotRequired["aws_sdk_bedrock.types.job_status_details.JobStatusDetails"]
    """<p>The status of the validation sub-task of the job.</p>"""
    creation_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The start time of the validation sub-task of the job.</p>"""
    last_modified_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The latest update to the validation sub-task of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationDetails) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_bedrock.types.job_status_details

        out["status"] = aws_sdk_bedrock.types.job_status_details.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["lastModifiedTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> ValidationDetails:
    out: ValidationDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock.types.job_status_details

        out["status"] = aws_sdk_bedrock.types.job_status_details.deserialize_json(
            data["status"]
        )
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["last_modified_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    return out
