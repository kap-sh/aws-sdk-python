"""Generated from Smithy shape ``com.amazonaws.securityagent#DocumentInfo``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DocumentInfo(TypedDict):
    s3_location: NotRequired["str"]
    """<p>The Amazon S3 location of the document.</p>"""
    artifact_id: NotRequired["str"]
    """<p>The unique identifier of the artifact associated with the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentInfo) -> dict:
    out: dict = {}
    if "s3_location" in value:
        out["s3Location"] = value["s3_location"]
    if "artifact_id" in value:
        out["artifactId"] = value["artifact_id"]
    return out


def deserialize_json(data: dict) -> DocumentInfo:
    out: DocumentInfo = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        out["s3_location"] = data["s3Location"]
    if "artifactId" in data:
        out["artifact_id"] = data["artifactId"]
    return out
