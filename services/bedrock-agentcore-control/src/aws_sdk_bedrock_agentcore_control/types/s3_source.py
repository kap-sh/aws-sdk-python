"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.s3_uri


class S3Source(TypedDict, closed=True):
    s3_uri: "aws_sdk_bedrock_agentcore_control.types.s3_uri.S3Uri"
    """<p> Amazon S3 URI of the JSONL file (for example, <code>s3://my-bucket/path/to/examples.jsonl</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3Source:
    out: S3Source = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("S3Source.s3_uri required")
    return out
