"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalFlowNodeS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_s3_bucket_name


class RetrievalFlowNodeS3Configuration(TypedDict, closed=True):
    bucket_name: "capo_bedrock_agent.types.flow_s3_bucket_name.FlowS3BucketName"
    """<p>The name of the Amazon S3 bucket from which to retrieve data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFlowNodeS3Configuration) -> dict:
    out: dict = {}
    out["bucketName"] = value.get("bucket_name", "")
    return out


def deserialize_json(data: dict) -> RetrievalFlowNodeS3Configuration:
    out: RetrievalFlowNodeS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    return out
