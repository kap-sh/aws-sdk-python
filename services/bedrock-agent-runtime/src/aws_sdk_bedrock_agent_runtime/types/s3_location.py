"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#S3Location``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.s3_uri


class S3Location(TypedDict):
    uri: "aws_sdk_bedrock_agent_runtime.types.s3_uri.S3Uri"
    """<p>The path to the Amazon S3 bucket where the image is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("S3Location.uri required")
    return out
