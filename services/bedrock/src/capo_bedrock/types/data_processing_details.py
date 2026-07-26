"""Generated from Smithy shape ``com.amazonaws.bedrock#DataProcessingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.job_status_details
    import capo_bedrock.types.timestamp


class DataProcessingDetails(TypedDict, closed=True):
    status: NotRequired["capo_bedrock.types.job_status_details.JobStatusDetails"]
    """<p>The status of the data processing sub-task of the job.</p>"""
    creation_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The start time of the data processing sub-task of the job.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The latest update to the data processing sub-task of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProcessingDetails) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_bedrock.types.job_status_details

        out["status"] = capo_bedrock.types.job_status_details.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import capo_bedrock.types.timestamp

        out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> DataProcessingDetails:
    out: DataProcessingDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_bedrock.types.job_status_details

        out["status"] = capo_bedrock.types.job_status_details.deserialize_json(
            data["status"]
        )
    if "creationTime" in data:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastModifiedTime" in data:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    return out
