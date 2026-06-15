"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJob``."""

from typing import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError


class ExtractionJob(TypedDict):
    job_id: "str"
    """<p>The unique identifier of the extraction job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJob) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> ExtractionJob:
    out: ExtractionJob = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("ExtractionJob.job_id required")
    return out
