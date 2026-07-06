"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StorageFlowNodeS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_s3_bucket_name


class StorageFlowNodeS3Configuration(TypedDict, closed=True):
    bucket_name: "aws_sdk_bedrock_agent.types.flow_s3_bucket_name.FlowS3BucketName"
    """<p>The name of the Amazon S3 bucket in which to store the input into the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageFlowNodeS3Configuration) -> dict:
    out: dict = {}
    out["bucketName"] = value.get("bucket_name", "")
    return out


def deserialize_json(data: dict) -> StorageFlowNodeS3Configuration:
    out: StorageFlowNodeS3Configuration = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    return out
