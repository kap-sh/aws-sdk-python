"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#S3ObjectFile``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.s3_uri


class S3ObjectFile(TypedDict):
    uri: "aws_sdk_bedrock_agent_runtime.types.s3_uri.S3Uri"
    """<p>The uri of the s3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectFile) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3ObjectFile:
    out: S3ObjectFile = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("S3ObjectFile.uri required")
    return out
