"""Generated from Smithy shape ``com.amazonaws.bedrockagent#S3VectorsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.index_arn
    import aws_sdk_bedrock_agent.types.index_name
    import aws_sdk_bedrock_agent.types.vector_bucket_arn


class S3VectorsConfiguration(TypedDict, closed=True):
    vector_bucket_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket where vector embeddings are stored. This bucket contains the vector data used by the knowledge base.</p>"""
    index_arn: NotRequired["aws_sdk_bedrock_agent.types.index_arn.IndexArn"]
    """<p>The Amazon Resource Name (ARN) of the vector index used for the knowledge base. This ARN identifies the specific vector index resource within Amazon Bedrock.</p>"""
    index_name: NotRequired["aws_sdk_bedrock_agent.types.index_name.IndexName"]
    """<p>The name of the vector index used for the knowledge base. This name identifies the vector index within the Amazon Bedrock service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3VectorsConfiguration) -> dict:
    out: dict = {}
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    return out


def deserialize_json(data: dict) -> S3VectorsConfiguration:
    out: S3VectorsConfiguration = {}  # type: ignore[typeddict-item]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    return out
