"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#S3Location``."""

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class S3Location(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the Amazon S3 bucket where the resource is stored.</p>"""
    prefix: "str"
    """<p>The name of the Amazon S3 prefix/key where the resource is stored.</p>"""
    version_id: NotRequired["str"]
    """<p>The name of the Amazon S3 version ID where the resource is stored (Optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["prefix"] = value["prefix"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3Location.bucket required")
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError("S3Location.prefix required")
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    return out
