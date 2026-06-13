"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#S3ObjectDoc``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.s3_uri


class S3ObjectDoc(TypedDict):
    uri: "aws_sdk_bedrock_agent_runtime.types.s3_uri.S3Uri"
    """<p>The file location of the S3 wrapper object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectDoc) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3ObjectDoc:
    out: S3ObjectDoc = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("S3ObjectDoc.uri required")
    return out
